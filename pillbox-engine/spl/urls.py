# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from spl import views

# urlpatterns = [
#     url(r'sync/(?P<action>\w+)/$', views.SyncSpl.as_view()),
#     url(r'sync/(?P<action>\w+)/$', views.SyncSpl.as_view()),
#     # url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

router = DefaultRouter()
router.register(r'sync', views.SyncSpl, base_name='sync')
# router.register(r'sync/pills', views.SyncSpl, base_name='sync-pills')
urlpatterns = router.urls
