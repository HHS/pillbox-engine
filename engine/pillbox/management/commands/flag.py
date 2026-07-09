from __future__ import print_function

import re
import os
import time
import traceback
from django.utils import timezone
from django.core.management.base import BaseCommand

from pillbox.models import PillBoxData

class BreakIt(Exception): pass

class Command(BaseCommand):
    help = 'Syncing has_pillbox_value with based on the content of the table'

    def handle(self, *args, **options):
        print(self.help)

        pills = PillBoxData.objects.all()
        all_fields = PillBoxData._meta.get_all_field_names()
        pillbox_fields = []

        for field in all_fields:
            if field.startswith('pillbox_'):
                pillbox_fields.append(field)

        pills.update(has_pillbox_value=False)
        for pill in pills:
            try:
                for field in pillbox_fields:
                    value = getattr(pill, field)
                    if value != '' and value is not None:
                        pill.has_pillbox_value = True
                        pill.save()
                        print('pill %s has pillbox value' % pill.id)
                        raise BreakIt

            except BreakIt:
                pass

        pills = PillBoxData.objects.all()
        has_value = pills.filter(has_pillbox_value=True).count()
        no_value = pills.filter(has_pillbox_value=False).count()

        print('Has pillbox value: %s' % has_value)
        print('Does Not have pillbox value: %s' % no_value)
