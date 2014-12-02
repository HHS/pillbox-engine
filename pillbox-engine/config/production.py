# -*- coding: utf-8 -*-
'''
Production Configurations
'''
from configurations import values


from .common import Common


class Production(Common):

    # INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    # END INSTALLED_APPS

    # Mail settings
    EMAIL_HOST = "localhost"
    EMAIL_PORT = 1025
    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')
    # End mail settings

    # SITE CONFIGURATION
    # Hosts/domain names that are valid for this site
    # See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["*"]
    # END SITE CONFIGURATION

    INSTALLED_APPS += ("gunicorn", )

    # Your production stuff: Below this line define 3rd party libary settings
    BROKER_URL = 'amqp://localhost'
    CELERY_RESULT_BACKEND = 'amqp'
