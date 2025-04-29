from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SharingViewSet

router = DefaultRouter()
router.register(r"", SharingViewSet, basename="sharing")

urlpatterns = router.urls
