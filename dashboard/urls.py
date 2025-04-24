from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DashboardView, BotChannelsViewSet, BotsAgentViewSet

router = DefaultRouter()
router.register(r"channels", BotChannelsViewSet)
router.register(r"bots", BotsAgentViewSet, basename="bots")

urlpatterns = router.urls + [
    path("", DashboardView.as_view(), name="dashboard"),
]
