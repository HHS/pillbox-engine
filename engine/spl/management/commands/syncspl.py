from __future__ import print_function

from django.core.management.base import BaseCommand

from spl.sync.controller import Controller


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
                controller = Controller(stdout=self.stdout)
                controller.sync(args[0])
