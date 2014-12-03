from rest_framework.routers import DefaultRouter
from spl import views

router = DefaultRouter()
router.register(r'sync', views.SyncSpl, base_name='sync')
urlpatterns = router.urls
