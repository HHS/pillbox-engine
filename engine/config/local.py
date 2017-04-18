# -*- coding: utf-8 -*-
'''
Local Configurations

- Runs in Debug mode
- Uses console backend for emails
- Use Django Debug Toolbar
'''
import environ
BASE_DIR = environ.Path(__file__) - 1  # (/a/myfile.py - 2 = /)

from .common import *  # noqa


# DEBUG
DEBUG = env.bool('DEBUG', True)
TEMPLATE_DEBUG = DEBUG
# END DEBUG

# django-debug-toolbar
MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar',)

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}
# end django-debug-toolbar

# Your local stuff: Below this line define 3rd party libary settings
