from __future__ import print_function

import os
import sys
import time
import fnmatch

from django.conf import settings
from django.core.management.base import BaseCommand

from spl.models import SetInfo, ProductData, Source, Ingredient
from spl.management.xpath import XPath


class Command(BaseCommand):
    args = '<products> | <pills> | <all>'
    help = 'Add/Update SPL data'

    def handle(self, *args, **options):
        """ Options currently handle: products, pills, all
        all will combine products and pills actions
        """

        arguments = ['products', 'pills', 'all']

        if args:
            if args[0] in arguments:
                self._update(args[0])

    def _update(self, action):
        start = time.time()

        x = XPath()

        sources = Source.objects.all().values('title')

        folders = [s['title'] for s in sources]

        counter = {
            'added': 0,
            'updated': 0
        }

        for folder in folders:
            # d = '%s/tmp-unzipped/%s' % (settings.BASE_DIR, folder)
            d = '%s/%s' % (settings.SPL_RAW_DATA, folder)
            files = os.listdir(d)

            for f in files:
                if fnmatch.fnmatch(f, '*.xml'):
                    output = getattr(x, action)(f, d)
                    if output:
                        counter = getattr(self, '_%s' % action)(output, counter)

                    self.stdout.write('added:%s | updated:%s | error:%s | skipped: %s' %
                                      (counter['added'], counter['updated'], x.error, x.skip), ending='\r')
                    sys.stdout.flush()

        end = time.time()

        self.stdout.write(self._time_spent(start, end))

    def _all(self, data, counter):
        """ Triggers and manages products and pill methods """

        counter = self._products(data['products'], counter)
        counter = self._pills(data['pills'], counter)

        return counter

    def _products(self, data, counter):

        setid = data['setid']
        data.pop('setid')

        updated_values = data

        obj, created = SetInfo.objects.update_or_create(setid=setid, defaults=updated_values)

        if created:
            counter['added'] += 1
        elif obj:
            counter['updated'] += 1

        return counter

    def _pills(self, data_set, counter):

        for data in data_set:
            id = data['id']
            data.pop('id')

            ingredients = data['ingredients']
            data.pop('ingredients')

            # Update ingredients
            for item in ingredients:
                ingredient_id = item['id']
                updated_values = {
                    'code_system': item['code_system'],
                    'name': item['name'],
                    'class_code': item['class_code']
                }

                obj, created = Ingredient.objects.get_or_create(id=ingredient_id, defaults=updated_values)

            # Update pills
            updated_values = data

            obj, created = ProductData.objects.update_or_create(id=id, defaults=updated_values)

            if created:
                counter['added'] += 1
            elif obj:
                counter['updated'] += 1

        return counter

    def _time_spent(self, start, end):

        spent = end - start
        minutes = spent / 60
        seconds = spent % 60

        return '\nTime spent : %s minues and %s seconds' % (int(minutes), round(seconds, 2))
