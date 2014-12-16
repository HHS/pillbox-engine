from __future__ import division
import csv

from pillbox.models import PillBoxData, Shape, Color
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
    reader = csv.reader(csv_file, delimiter=',')

    headers = reader.next()

    pillbox_map = {
        'spp': 'setid',
        'SETID': 'setid_product',
        'author_type': 'author_type',
        'FILE_NAME': 'file_name',
        'LABEL_EFFECTIVE_TIME': 'effective_time',
        'PRODUCT_CODE': 'produce_code',
        'NDC9': 'ndc9',
        'PART_NUM': 'part_num',
        'MEDICINE_NAME': 'medicine_name',
        'PART_MEDICINE_NAME': 'part_medicine_name',
        'author': 'author',
        'SPLIMPRINT': 'splimprint',
        'PILLBOX_IMPRINT': 'pillbox_imprint',
        'SPLCOLOR': 'splcolor',
        'SPLCOLOR_TEXT': 'splcolor_text',
        'PILLBOX_COLOR_TEXT': 'pillbox_color_text',
        'SPLSHAPE': 'splshape',
        'SPLSHAPE_TEXT': 'splshape_text',
        'PILLBOX_SHAPE_TEXT': 'pillbox_shape_text',
        'SPLSCORE': 'splscore',
        'PILLBOX_SCORE': 'pillbox_score',
        'SPLSIZE': 'splsize',
        'PILLBOX_SIZE': 'pillbox_size',
        'DEA_SCHEDULE_CODE': 'dea_schedule_code',
        'SPL_INACTIVE_ING': 'spl_inactive_ing',
        'RXCUI': 'rxcui',
        'RXTTY': 'rxtty',
        'RXSTRING': 'rxstring',
        'image_id': 'splimage',
        'HAS_IMAGE': 'has_image',
        'INGREDIENTS': '',
        'SPL_INGREDIENTS': 'spl_ingredients',
        'PROD_MEDICINES_PRIKEY': '',
        'DOSAGE_FORM': 'dosage_form',
        'SPL_STRENGTH': 'spl_strength',
        'RXNORM_SOURCE': '',
        'SPL_ID': '',
        'source': 'source',
        'document_type': 'document_type',
        'ACTIVE_MOEITY': '',
        'MARKETING_ACT_CODE': 'marketing_act_code',
        'APPROVAL_CODE': 'approval_code',
        'IMAGE_SOURCE': 'image_source',
        'EQUAL_PRODUCT_CODE': 'equal_product_code',
        'VERSION_NUMBER': 'version_number',
        'SPLIMPRINT_orig': '',
        'SPLCOLOR_orig': '',
        'SPLSHAPE_orig': '',
        'SPLSCORE_orig': '',
        'SPLSIZE_orig': '',
        'NO_RXCUI': '',
        'FROM_SIS': 'from_sis',
        'SPLIMPRINT_changeCode': '',
        'SPLCOLOR_changeCode': '',
        'SPLSHAPE_changeCode': '',
        'SPLSCORE_changeCode': '',
        'SPLSIZE_changeCode': '',
    }

    new_header = []
    for i in headers:
        new_header.append(pillbox_map[i])

    # Check if splcolor_text and splshape_text are in the import file
    # if they are not populate the text with the value of the code box
    if 'PILLBOX_COLOR_TEXT' not in headers:
        color_from_code = True

    if 'PILLBOX_SHAPE_TEXT' not in headers:
        shape_from_code = True

    compatibility = {}
    if 'PILLBOX_IMPRINT' not in headers:
        compatibility['splimprint'] = 'pillbox_imprint'

    if 'PILLBOX_SCORE' not in headers:
        compatibility['splscore'] = 'pillbox_score'

    if 'PILLBOX_SIZE' not in headers:
        compatibility['splsize'] = 'pillbox_size'

    counter = {
        'added': 0,
        'updated': 0
    }

    for line in reader:
        new = {}
        for k, v in enumerate(new_header):
            # if column doesn't exist just pass
            try:
                new[v] = line[k]

                ## Populate color text based on color code
                if v == 'splcolor' and color_from_code:
                    try:
                        if line[k]:
                            codes = line[k].split(';')
                            colors = Color.objects.filter(code__in=codes).values('display_name')
                        new['splcolor_text'] = ";".join([c['display_name'] for c in colors])
                    except Color.DoesNotExist:
                        pass

                # Populate shape text based on shape code
                if v == 'splshape' and shape_from_code:
                    try:
                        if line[k]:
                            shape = Shape.objects.get(code=line[k])
                            new['splshape_text'] = shape.display_name
                    except Shape.DoesNotExist:
                        pass

                # If dataset doesn't include pillbox variables populate fields with SPL data
                if v in compatibility:
                    new[compatibility[v]] = line[k]

            except KeyError:
                pass

        new.pop('')

        setid = new['setid'].replace('_', '-').replace(' ', '')
        new.pop('setid')

        if new['has_image'] == '1':
            new['has_image'] = True
        else:
            new['has_image'] = False

        if new['splimage']:
            new['splimage'] = 'pillbox/' + new['splimage'] + '.jpg'

        obj, created = PillBoxData.objects.update_or_create(setid=setid, defaults=new)

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
