
from rest_framework.routers import DefaultRouter
from .views import PostUploadViewSet

router = DefaultRouter()
router.register(r'posts', PostUploadViewSet, basename='posts')

urlpatterns = router.urls  # yeh pehle se router ki urls le lega