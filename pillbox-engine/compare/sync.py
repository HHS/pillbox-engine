from __future__ import print_function, division
import sys
from spl.models import Pill, Task
from pillbox.models import PillBoxData
from compare.models import Color, Score, Size, Shape, Imprint, Image


def compare(task_id):

    task = Task.objects.get(pk=task_id)
    task.status = 'TRANSFERING'
    task.save()

    percent = 0
    interval = 0

    # reset all the records
    PillBoxData.objects.all().update(updated=False, stale=False, new=False)

    spl_pills = Pill.objects.all()
    total = spl_pills.count()

    counter = {
        'exist': 0,
        'new': 0
    }
    for pill in spl_pills:

        try:
            pillbox = PillBoxData.objects.get(setid=pill.ssp)
            counter['exist'] += 1
            pillbox.updated = True
            pillbox.save()
            update(pillbox, pill)

        except PillBoxData.DoesNotExist:
            counter['new'] += 1
            pillbox = PillBoxData()
            pillbox.new = True
            update(pillbox, pill)

        processed = counter['exist'] + counter['new']
        percent = round((processed/total)*100, 2)

        if int(percent) > interval:
            interval = int(percent)

            meta = {'updated': counter['exist'],
                    'new': counter['new'],
                    'action': 'transfer',
                    'percent': percent}
            task.meta.update(meta)
            task.save()

        print(counter, end='\r')
        sys.stdout.flush()

    #flag stale records
    PillBoxData.objects.filter(new=False, updated=False).update(stale=True)

    print(counter)


def update(pillbox, spl_pill, action='new'):

    pillbox_pill_map = {
        'ssp': 'setid',
        'produce_code': 'produce_code',
        'ndc9': 'ndc9',
        'part_num': 'part_num',
        'medicine_name': 'medicine_name',
        'part_medicine_name': 'part_medicine_name',
        'dea_schedule_code': 'dea_schedule_code',
        'spl_inactive_ing': 'spl_inactive_ing',
        'spl_ingredients': 'spl_ingredients',
        'rxcui': 'rxcui',
        'rxtty': 'rxtty',
        'rxstring': 'rxstring',
        'dosage_form': 'dosage_form',
        'spl_strength': 'spl_strength',
        'marketing_act_code': 'marketing_act_code',
        'approval_code': 'approval_code',
        'equal_product_code': 'equal_product_code',
    }

    pillbox_product_map = {
        'setid': 'setid_product',
        'filename': 'file_name',
        'effective_time': 'effective_time',
        'source': 'source',
        'version_number': 'version_number',

    }

    check_map = {
        'splimprint': Imprint,
        'splcolor': Color,
        'splscore': Score,
        'splshape': Shape,
        'splsize': Size,
        'splimage': Image,
    }

    for key, value in pillbox_pill_map.iteritems():
        setattr(pillbox, value, getattr(spl_pill, key))

    for key, value in pillbox_product_map.iteritems():
        setattr(pillbox, value, getattr(spl_pill.setid, key))

    if spl_pill.setid.author_legal:
        pillbox.author_type = 'LEGAL'
        pillbox.author = spl_pill.setid.author_legal
    else:
        pillbox.author_type = 'LABELER'
        pillbox.author = spl_pill.setid.author

    if action == 'new':
        # add items to the pillboxdata model
        for key, value in check_map.iteritems():
            if key == 'splimage':
                if getattr(spl_pill, key):
                    pillbox.has_image = True
                    pillbox.image_source = 'NLM'
            setattr(pillbox, key, getattr(spl_pill, key))

        # for new items with need to save first to get a pillbox id
        pillbox.save()

        for key, value in check_map.iteritems():
            new_value = getattr(spl_pill, key)
            if new_value:
                new_obj = value()
                new_obj.spl_value = new_value
                new_obj.pillbox_value = new_value
                new_obj.spl_id = spl_pill.id
                new_obj.pillbox_id = pillbox.id

                new_obj.save()

    else:
        pillbox.save()
        for key, value in check_map.iteritems():
            spl_value = getattr(spl_pill, key)
            pillbox_value = getattr(pillbox, key)

            if spl_value != pillbox_value and pillbox_value:

                # Check if there is a record already
                try:
                    obj = value.objects.get(spl=spl_pill.id, pillbox=pillbox.id)
                    obj.spl_value = spl_value
                    obj.pillbox_value = pillbox_value
                    obj.is_different = True
                    obj.save()

                except value.DoesNotExist:
                    new_obj = value()
                    new_obj.spl_value = new_value
                    new_obj.pillbox_value = new_value
                    new_obj.spl_id = spl_pill.id
                    new_obj.pillbox_id = pillbox.id
                    new_obj.is_different = True

                    new_obj.save()


def clear_compare_tables():
    """ Delete all records in compare tables (FOR DEV ONLY) """

    Imprint.objects.all().delete()
    Color.objects.all().delete()
    Score.objects.all().delete()
    Shape.objects.all().delete()
    Size.objects.all().delete()
    Image.objects.all().delete()
