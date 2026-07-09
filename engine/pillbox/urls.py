from rest_framework.routers import DefaultRouter
from pillbox import views

router = DefaultRouter()
router.register(r'status', views.ImportStatus, base_name='status')
router.register(r'export_status', views.ExportStatus, base_name='export_status')
router.register(r'transfer', views.Transfer, base_name='transfer')
urlpatterns = router.urls
