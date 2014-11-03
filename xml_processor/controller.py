from __future__ import print_function

import os
import time
import fnmatch
from spl.models import SetInfo, Source
from xpath import XPath

from django.conf import settings


def udpate_setinfo():

    start = time.time()

    x = XPath()

    # d = '../tmp-unzipped/HRX'
    # x.parse('0548145e-6b20-4843-9bcc-cf270ea2f072.xml', d)
    # x.test('0548145e-6b20-4843-9bcc-cf270ea2f072.xml', d)

    folders = Source.objects.all().value('title')

    added = 0
    updated = 0

    for folder in folders:
        d = '%s/tmp-unzipped/%s' % (settings.BASE_DIR, folder['title'])
        files = os.listdir(d)

        for f in files:
            if fnmatch.fnmatch(f, '*.xml'):
                output = x.parse_set_info(f, d)
                if output:
                    setid = output['setid']
                    output.pop('setid')

                    updated_values = output

                    obj, created = SetInfo.objects.update_or_create(setid=setid, defaults=updated_values)

                    if created:
                        added += 1
                    else:
                        updated += 1

                print('added:%s | updated:%s | error:%s' % (added, updated, x.error), end='\r')

    # print('\nErrors: %s' % x.error)
    # x.parse("0013824B-6AEE-4DA4-AFFD-35BC6BF19D91.xml")
    # x.parse('006572e2-0f86-4be3-81cd-91e230cce852.xml')

    # print x.get_source('../tmp-unzipped/HRX')
    end = time.time()

    print('\nTime spent : %s seconds' % (end - start))
