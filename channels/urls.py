from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChannelViewSet

router = DefaultRouter()
router.register(r"", ChannelViewSet, basename="channels")

urlpatterns = router.urls
