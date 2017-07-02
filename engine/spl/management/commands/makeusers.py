from __future__ import print_function

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Permission, Group
from django.db import IntegrityError


class Command(BaseCommand):
    help = 'Create Pillbox Users'

    def handle(self, *args, **options):

        # Create Admin
        try:
            user = User.objects.create_user('admin', 'admin@example.com', 'admin')
            user.is_superuser = True
            user.is_staff = True
            user.save()
        except IntegrityError:
            pass

        # Pillbox Group
        try:
            group = Group()

            group.name = 'Pillbox'
            group.save()
        except IntegrityError:
            # Group already exists, so just pass
            group = Group.objects.filter(name='Pillbox')[:1].get()

        # Grab need permission ids
        permissions = Permission.objects.all()

        for p in permissions:
            if p.content_type.model not in ['group', 'permission', 'user']:
                if 'add' not in p.name or (p.content_type.model == 'import' and 'add' in p.name):
                    group.permissions.add(p)

        # Create Pillbox User
        try:
            user = User.objects.create_user('pillbox', 'pillbox@example.com', 'pillbox')
            user.is_staff = True
            user.groups.add(group)
            user.save()
        except IntegrityError:
            # User already exists, so just passs
            pass


