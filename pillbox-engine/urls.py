# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
# from django.contrib.staticfiles import views

import spl.urls
import pillbox.urls

import xadmin
xadmin.autodiscover()

 # Version module automatically registration required version control Model
from xadmin.plugins import xversion
xversion.register_models()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^spl/', include(spl.urls)),
    url(r'^pillbox/', include(pillbox.urls)),
    url(r'^', include(xadmin.site.urls)),
    # Your stuff: custom urls go here

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

### This hack let static files be served with DEBUG false
if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
