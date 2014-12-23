from __future__ import division
import csv

from pillbox.models import PillBoxData
from spl.models import Task


def importer(csv_path, task_id=None):

    update_interval = 0
    processed = 0
    total = 0

    # Count number of lines

    with open(csv_path) as f:
        for line in f:
            total += 1

    task = Task.objects.get(pk=task_id)
    task.status = 'IMPORT'
    task.meta.update({
        'added': 0,
        'updated': 0,
        'error': 0,
        'action': 'import',
        'percent': 0
    })
    task.save()

    csv_file = open(csv_path, 'r')
    reader = csv.DictReader(csv_file, delimiter=',')

    pillbox_map = {
        'setid': 'setid_product',
        'label_effective_time': 'effective_time',
        'product_code': 'produce_code',
        'image_id': 'splimage',
        'epc_match': 'from_sis',
    }

    pillbox_fields = PillBoxData._meta.get_all_field_names()

    counter = {
        'added': 0,
        'updated': 0
    }

    for line in reader:
        line_copy = line.copy()

        # Grap spp first
        setid = line_copy['spp'].replace('_', '-').replace(' ', '')

        line_copy.pop('spp')

        # if 'pillbox_color_text' not in line:

        for k, v in line.iteritems():
            # Check if key is in column map
            key = k.lower()
            if key in pillbox_map:
                line_copy.pop(k)
                line_copy[pillbox_map[key]] = v

            # Remove keys that are not a field
            if key not in pillbox_fields:
                try:
                    line_copy.pop(k)
                except KeyError:
                    # If the key is already removed just pass
                    pass

        update_dict = {}
        # Make all keys lower cased
        for k, v in line_copy.iteritems():
            update_dict[k.lower()] = v

        if update_dict['has_image'] == '1':
            update_dict['has_image'] = True
        elif update_dict['has_image'] == '0':
            update_dict['has_image'] = False

        if update_dict['splimage']:
            # Add pillbox folder path if not already there
            if 'pillbox/' != update_dict['splimage'][:8]:
                update_dict['splimage'] = 'pillbox/' + update_dict['splimage']

            # Add jpg format if the value doesn't include format
            if '.' != update_dict['splimage'][-4:-3]:
                update_dict['splimage'] = update_dict['splimage'] + '.jpg'

        obj, created = PillBoxData.objects.update_or_create(setid=setid, defaults=update_dict)

        if created:
            counter['added'] += 1
        else:
            counter['updated'] += 1

        processed = counter['added'] + counter['updated']
        percent = round((processed / total) * 100, 2)

        ## To decrease the number of times the database is called, update meta data
        ## in integer intervals
        if int(percent) > update_interval:
            update_interval = percent
            task.meta['added'] = counter['added']
            task.meta['updated'] = counter['updated']
            task.meta['percent'] = percent
            task.save()

    return counter
