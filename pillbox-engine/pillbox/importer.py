import csv
import time

from pillbox.models import PillBoxData, Import


def importer(csv_path, import_id=None, task_obj=None):

    start = time.time()

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
        'SPLCOLOR': 'splcolor',
        'SPLSCORE': 'splscore',
        'SPLSHAPE': 'splshape',
        'SPLSIZE': 'splsize',
        'DEA_SCHEDULE_CODE': 'dea_schedule_code',
        'SPL_INACTIVE_ING': 'spl_inactive_ing',
        'RXCUI': 'rxcui',
        'RXTTY': 'rxtty',
        'RXSTRING': 'rxstring',
        'image_id': 'image_id',
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
            except KeyError:
                pass

        new.pop('')

        setid = new['setid'].replace('_', '-').replace(' ', '')
        new.pop('setid')
        print new
        obj, created = PillBoxData.objects.update_or_create(setid=setid, defaults=new)

        if created:
            counter['added'] += 1
        else:
            counter['updated'] += 1

        if task_obj:
            task_obj.update_state(state='PROGRESS',
                                  meta={'added': counter['added'],
                                        'updated': counter['updated'],
                                        'action': 'pillbox_import'})

    end = time.time()
    spent = end - start

    if import_id:
        import_obj = Import.objects.get(pk=import_id)
        import_obj.completed = True
        import_obj.status = 'SUCCESSFUL'
        import_obj.duration = spent
        import_obj.added = counter['added']
        import_obj.updated = counter['updated']
        import_obj.save()

    return counter
