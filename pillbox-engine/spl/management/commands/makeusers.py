from __future__ import print_function

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create Pillbox Users'

    def handle(self, *args, **options):

        # Create Admin
        user = User.objects.create_user('admin', 'admin@example.com', 'admin')
        user.is_superuser = True
        user.is_staff = True
        user.save()

        # Create Pillbox User
        user = User.objects.create_user('pillbox', 'pillbox@example.com', 'pillbox')
        user.is_staff = True
        user.save()
