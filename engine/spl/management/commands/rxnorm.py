from __future__ import print_function

from django.core.management.base import BaseCommand

from spl.tasks import rxnorm_task
from spl.sync.controller import Controller


class Command(BaseCommand):
    help = 'Execute RxNorm'

    def handle(self, *args, **options):
        """ Options currently handle: products, pills, all
        all will combine products and pills actions
        """

        rxnorm_task()
