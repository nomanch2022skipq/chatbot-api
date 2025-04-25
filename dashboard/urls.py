from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BotsAgentViewMessages, DashboardView, BotChannelsViewSet, BotsAgentViewSet

router = DefaultRouter()
router.register(r"channels", BotChannelsViewSet)
router.register(r"bots", BotsAgentViewSet, basename="bots")
router.register(r"messages", BotsAgentViewMessages, basename="messages")

urlpatterns = router.urls + [
    path("", DashboardView.as_view(), name="dashboard"),
]
