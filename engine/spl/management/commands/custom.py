from __future__ import print_function

from django.core.management.base import BaseCommand

from spl.sync.xpath import XPath


class Command(BaseCommand):
    help = 'Add/Update SPL data'

    def handle(self, *args, **options):
        """ Options currently handle: products, pills, all
        all will combine products and pills actions
        """
        x = XPath()

        v = x.pills('3ebf893d-2100-40c7-8e8f-5fa1b2da41a2.xml', '/pillbox/downloads/unzip/ANIMAL/')
        print(v[0]['splimprint'])
        print('\n' in v[0]['splimprint'])
