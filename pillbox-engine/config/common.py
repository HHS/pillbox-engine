# -*- coding: utf-8 -*-
"""
Django settings for pillbox-engine project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# import os

from __future__ import absolute_import, unicode_literals
from os.path import join, dirname
import environ

BASE_DIR = environ.Path(__file__) - 2  # (/a/myfile.py - 2 = /)

env = environ.Env()


# DEBUG
DEBUG = env.bool('DEBUG', default=True)
# END DEBUG

# APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    'django.contrib.humanize',

    # Admin
    'django.contrib.admin',
)
THIRD_PARTY_APPS = (
    'xadmin',
    # 'reversion',
    'crispy_forms',
    # 'kombu.transport.django',
    'rest_framework',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    # Your stuff: custom apps go here
    'spl',
    'pillbox',
    'compare',
    # 'djcelery_pillbox'
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
# END APP CONFIGURATION

# MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
# END MIDDLEWARE CONFIGURATION

# MIGRATIONS CONFIGURATION
# MIGRATION_MODULES = {
    # 'sites': 'contrib.sites.migrations'
# }
# END MIGRATIONS CONFIGURATION

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# END DEBUG

# SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
#       In production, this is changed to a values.SecretValue() setting
SECRET_KEY = "changemetosomethingsecure!"
# END SECRET CONFIGURATION

# FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    str(BASE_DIR.path('fixtures')),
)
# END FIXTURE CONFIGURATION

# MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ("""Change ME""", 'email@example.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# END MANAGER CONFIGURATION

# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': env.db("DATABASE_URL", default='sqlite:///%s' % str(BASE_DIR.path('db/db.sqlite3'))),
}
# END DATABASE CONFIGURATION

# GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'America/New_York'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# END GENERAL CONFIGURATION

# TEMPLATE CONFIGURATION
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
    'DIRS': [
        str(BASE_DIR.path('templates')),
    ],
    'OPTIONS': {
        'debug': DEBUG,
        'context_processors': [
            'django.contrib.auth.context_processors.auth',
            'django.core.context_processors.debug',
            'django.core.context_processors.i18n',
            'django.core.context_processors.media',
            'django.core.context_processors.static',
            'django.core.context_processors.tz',
            'django.contrib.messages.context_processors.messages',
            'django.core.context_processors.request',
        ],
    },
}]

# STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(BASE_DIR.path('staticfiles'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    str(BASE_DIR.path('static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
# END STATIC FILE CONFIGURATION

# MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(BASE_DIR.path('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
# END MEDIA CONFIGURATION

# URL Configuration
ROOT_URLCONF = 'urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'wsgi.application'
# End URL Configuration

# AUTHENTICATION CONFIGURATION
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)

# Custom user app defaults
# Select the correct user model
# AUTH_USER_MODEL = "users.User"
# END Custom user app defaults

# LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
# END LOGGING CONFIGURATION

# Your common stuff: Below this line define 3rd party library settings
# Celery settings

# BROKER_URL = values.Value('django://')
# CELERY_RESULT_BACKEND = values.Value('djcelery_pillbox.database:DatabaseBackend')
# CELERY_TASK_RESULT_EXPIRES = values.IntegerValue(3600)
# CELERY_DISABLE_RATE_LIMITS = values.BooleanValue(True)
# CELERYD_CONCURRENCY = values.IntegerValue(1)
# CELERY_ACCEPT_CONTENT = values.ListValue(['json', 'msgpack', 'yaml'])
# CELERY_TASK_SERIALIZER = values.Value('json')
# CELERY_RESULT_SERIALIZER = values.Value('json')
# CELERY_TRACK_STARTED = values.BooleanValue(True)
# CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True

DAILYMED_FTP_SITE = env.str('DAILYMED_FTP_SITE', 'public.nlm.nih.gov')
DAILYMED_FTP_PATH = env.str('DAILYMED_FTP_PATH', 'nlmdata/.dailymed/')
DAILYMED_FTP_USER = env.str('DAILYMED_FTP_USER', 'anonymous')
DAILYMED_FTP_PASS = env.str('DAILYMED_FTP_PASS', '')
DOWNLOAD_PATH = str(BASE_DIR.path('downloads/zip'))
SOURCE_PATH = str(BASE_DIR.path('downloads/unzip'))

