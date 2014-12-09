from rest_framework.routers import DefaultRouter
from pillbox import views

router = DefaultRouter()
router.register(r'status', views.ImportStatus, base_name='status')
urlpatterns = router.urls
