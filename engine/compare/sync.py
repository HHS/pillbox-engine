from __future__ import print_function, division
from spl.models import Pill, Task
from pillbox.models import PillBoxData
from compare.models import Color, Score, Size, Shape, Imprint, Image


def transfer_new(task_id):

    task = Task.objects.get(pk=task_id)
    task.status = 'TRANSFERING'
    meta = {'new': 0,
            'action': 'transfer',
            'percent': 0}
    task.meta.update(meta)
    task.save()

    percent = 0
    interval = 0

    # reset all the records
    PillBoxData.objects.all().update(new=False)

    spl_pills = Pill.objects.all()
    total = spl_pills.count()

    counter = 0
    print('transfering new pills')
    for pill in spl_pills:

        try:
            print('transferring %s' % pill.ssp)
            pillbox = PillBoxData.objects.get(setid=pill.ssp)

        except PillBoxData.DoesNotExist:
            pillbox = PillBoxData()
            pillbox.new = True
            update(pillbox, pill)

        counter += 1
        percent = round((counter/total)*100, 2)

        if int(percent) > interval:
            interval = int(percent)
            task.meta['percent'] = percent
            task.meta['new'] = counter
            task.save()
    print('Transfer completed')


def compare(task_id):

    print('Staring data compare')
    task = Task.objects.get(pk=task_id)
    task.status = 'COMPARING'
    meta = {'updated': 0,
            'action': 'transfer',
            'percent': 0}
    task.meta.update(meta)
    task.save()

    percent = 0
    interval = 0

    # reset all the records
    PillBoxData.objects.all().update(updated=False, stale=False)

    spl_pills = Pill.objects.all()
    total = spl_pills.count()

    counter = 0
    print('Getting all SPL pills')
    for pill in spl_pills:

        try:
            print('comparing %s' % pill.ssp)
            pillbox = PillBoxData.objects.get(setid=pill.ssp)
            counter += 1
            pillbox.updated = True
            pillbox.save()
            update(pillbox, pill, 'update')

        except PillBoxData.DoesNotExist:
            pass

        percent = round((counter/total)*100, 2)

        if int(percent) > interval:
            interval = int(percent)
            task.meta['percent'] = percent
            task.meta['updated'] = counter
            task.save()

    #flag stale records
    PillBoxData.objects.filter(updated=False, new=False).update(stale=True)
    print('Compare completed')


def update(pillbox, spl_pill, action='new'):

    pillbox_pill_map = {
        'ssp': 'setid',
        'produce_code': 'produce_code',
        'ndc9': 'ndc9',
        'part_num': 'part_num',
        'medicine_name': 'medicine_name',
        'part_medicine_name': 'part_medicine_name',
        'dea_schedule_code': 'dea_schedule_code',
        'dea_schedule_name': 'dea_schedule_name',
        'spl_inactive_ing': 'spl_inactive_ing',
        'spl_ingredients': 'spl_ingredients',
        'splcolor': 'splcolor',
        'splcolor_text': 'splcolor_text',
        'splshape': 'splshape',
        'splshape_text': 'splshape_text',
        'splsize': 'splsize',
        'splimprint': 'splimprint',
        'splscore': 'splscore',
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
        'splcolor_text': Color,
        'splscore': Score,
        'splshape_text': Shape,
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

        # add splimage if there is one
        if spl_pill.splimage:
            pillbox.has_image = True
            pillbox.image_source = 'SPL'
            pillbox.splimage = spl_pill.splimage.name

        # for new items with need to save first to get a pillbox id
        pillbox.save()

        ## only add to compare if there is an image
        if spl_pill.splimage:
            for key, value in check_map.iteritems():
                new_value = getattr(spl_pill, key)
                if new_value:
                    new_obj = value()
                    new_obj.spl_value = new_value
                    new_obj.spl_id = spl_pill.id
                    new_obj.pillbox_id = pillbox.id

                    new_obj.save()

    else:
        pillbox.save()

        for key, value in check_map.iteritems():

            if key == 'splimage':
                pillbox_key = key
            else:
                pillbox_key = key.replace('spl', 'pillbox_')

            spl_value = getattr(spl_pill, key)
            pillbox_value = getattr(pillbox, pillbox_key)

            #if values are the same get rid of pillbox data
            if spl_value == pillbox_value and key != 'splimage':
                setattr(pillbox, pillbox_key, None)
                pillbox.save()

            #only add if the values are different
            elif spl_value != pillbox_value and pillbox_value:
                #Only add if there is an image
                if pillbox.has_image:
                    # only add images that have values on both spl and pillbox
                    if key == 'splimage' and not spl_value:
                        continue

                    # Check if there is a record already
                    try:
                        obj = value.objects.get(spl=spl_pill.id, pillbox=pillbox.id)
                        obj.spl_value = spl_value
                        obj.pillbox_value = pillbox_value
                        obj.is_different = True
                        obj.save()

                    except value.DoesNotExist:
                        new_obj = value()
                        new_obj.spl_value = spl_value
                        new_obj.pillbox_value = pillbox_value
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


def test_update():
    pillbox = PillBoxData.objects.get(pk=292717)
    spl = Pill.objects.get(pk=120844)

    update(pillbox, spl, action='update')
