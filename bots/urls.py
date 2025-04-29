from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BotsAgentViewSet

router = DefaultRouter()
router.register(r"", BotsAgentViewSet, basename="bots")

urlpatterns = router.urls
