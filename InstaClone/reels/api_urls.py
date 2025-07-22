# reels/api_urls.py

from rest_framework.routers import DefaultRouter
from .views import ReelsViewSet

router = DefaultRouter()
router.register(r'reels', ReelsViewSet, basename='reels')

urlpatterns = router.urls


