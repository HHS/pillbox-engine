from django.conf.urls import patterns, include, url
# from django.contrib import admin

import xadmin
xadmin.autodiscover()

 # Version module automatically registration required version control Model
from xadmin.plugins import xversion
xversion.register_models()

from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pillbox_engine.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(xadmin.site.urls))
)
