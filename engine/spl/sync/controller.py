from __future__ import print_function, division
import shutil
import os
import sys
import time
import fnmatch

from django.conf import settings

from spl.models import Product, Pill, Source, Ingredient, Task
from spl.sync.xpath import XPath


class Controller(object):
    """ This class is specificaly written to work with celery task management """

    def __init__(self, task_id=None, stdout=None):
        self.stdout = stdout
        self.processed = 0
        self.total = 0
        self.action = None
        self.update_interval = 0
        try:
            self.task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            self.task = None

    def sync(self, action):
        """ Class's main method/hook for activating sync sequence

        @params
        - action: choices are pills | products | all
        """
        arguments = ['products', 'pills', 'all']

        if action in arguments:
            print('Starting SPL sync for %s' % action)
            self._update(action)

        return

    def _update(self, action):
        start = time.time()
        self.action = action

        x = XPath()

        sources = Source.objects.all()

        # self.total = sum([s.xml_count for s in sources if s.xml_count])

        # if action == 'pills':
            # there are fewer pills. 0.55 is a practical approximation of how many pills are in all xml files
            # self.total = self.total * 0.55

        # Make all discontinued to true to flag discontinued items
        if action == 'products':
            Product.objects.update(discontinued=True)

        counter = {
            'added': 0,
            'updated': 0
        }

        for source in sources:
            print('Updating source %s' % source)
            d = os.path.join(settings.SOURCE_PATH, source.title)
            try:
                files = os.listdir(d)
                self.total += len(files)

                for f in files:
                    print('Extracting %s info from %s' % (action, f))
                    self.processed += 1
                    if fnmatch.fnmatch(f, '*.xml'):
                        output = getattr(x, action)(f, d)
                        if output:
                            counter = getattr(self, '_%s' % action)(output, counter)


                        self._status(added=counter['added'], updated=counter['updated'],
                                     error=x.error, skipped=x.skip,
                                     action=action)
                # remove tmp2 folder
                if action == 'pills':
                    shutil.rmtree(os.path.join(d, 'tmp2'))

            except OSError:
                # IGNORE if the file doesn't exist
                pass

        end = time.time()

        self._time_spent(start, end)

        return

    def _all(self, data, counter):
        """ Triggers and manages products and pill methods """

        counter = self._products(data['products'], counter)
        counter = self._pills(data['pills'], counter)

        return counter

    def _products(self, data, counter):

        setid = data['setid']
        data.pop('setid')

        updated_values = data

        obj, created = Product.objects.update_or_create(setid=setid, defaults=updated_values)

        if created:
            counter['added'] += 1
        elif obj:
            counter['updated'] += 1

        return counter

    def _pills(self, data_set, counter):

        for data in data_set:
            ssp = data.pop('ssp')

            # Find the related product and get it's db id
            setid = data.pop('setid_id')
            try:
                product = Product.objects.get(setid=setid)
                product.is_osdf = True
                product.save()
                data['setid_id'] = product.id
            except Product.DoesNotExist:
                print('%s setid is not found' % setid)
                # go to the next round
                continue


            ingredients = data.pop('ingredients')

            data['spl_strength'] = ''
            data['spl_ingredients'] = ''
            data['spl_inactive_ing'] = ''

            for key, items in ingredients.iteritems():
                for item in items:
                    if key == 'active':
                        data['spl_strength'] += '%s %s %s;' % (item['name'],
                                                               item['numerator_value'],
                                                               item['numerator_unit'])
                        if 'active_moieties' in item:
                            active = item['active_moieties'][0]['name']
                        else:
                            active = ''
                        data['spl_ingredients'] += '%s[%s];' % (item['name'], active)

                    if key == 'inactive':
                        data['spl_inactive_ing'] += '%s;' % item['name']

                    ingredient_id = item['id']
                    updated_values = {
                        'code_system': item['code_system'],
                        'name': item['name'],
                        'class_code': item['class_code']
                    }

                    obj, created = Ingredient.objects.get_or_create(spl_id=ingredient_id, defaults=updated_values)

            # Update pills
            updated_values = data

            obj, created = Pill.objects.update_or_create(ssp=ssp, defaults=updated_values)

            if created:
                counter['added'] += 1
            elif obj:
                counter['updated'] += 1

        return counter

    def _time_spent(self, start, end):

        spent = end - start
        minutes = spent / 60
        seconds = spent % 60

        print('\nTime spent : %s minues and %s seconds' % (int(minutes), round(seconds, 2)))

        return

    def _status(self, **kwarg):

        print('inside status')
        percent = round((self.processed / self.total) * 100, 2)

        if self.task:

            ## To decrease the number of times the database is called, update meta data
            ## in integer intervals
            if (self.processed % 500) == 0.0:
                print('added:%s | updated:%s | error:%s | skipped: %s | percent: %s' %
                      (kwarg['added'], kwarg['updated'],
                       len(kwarg['error']), kwarg['skipped'], percent))
                meta = {'added': kwarg['added'],
                        'updated': kwarg['updated'],
                        'error': kwarg['error'],
                        'skipped': kwarg['skipped'],
                        'action': kwarg['action'],
                        'percent': percent}
                self.task.meta.update(meta)
                self.task.status = 'PROGRESS: SYNC %s' % kwarg['action']
                self.task.save()
        print('status updated')
