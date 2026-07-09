from __future__ import print_function

import re
import os
import time
import traceback
from django.utils import timezone
from django.core.management.base import BaseCommand

from pillbox.models import PillBoxData


class Command(BaseCommand):
    help = 'Execute RxNorm'

    def handle(self, *args, **options):
        print('Removing double spaces, extra tabs and extra line breaks')

        pills = PillBoxData.objects.all()

        for pill in pills:
            print('cleaning %s' % pill.setid)
            pill.spl_strength = re.sub('([\s]{2,})', ' ', pill.spl_strength)
            pill.spl_inactive_ing = re.sub('([\s]{2,})', ' ', pill.spl_inactive_ing)
            pill.medicine_name = pill.medicine_name.replace('\t', ' ')
            pill.splimprint = pill.splimprint.replace('\n', ' ')
            pill.save()
