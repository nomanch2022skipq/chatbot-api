from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DashboardView, DashboardStatsViewSet

router = DefaultRouter()
router.register(r"stats", DashboardStatsViewSet, basename="dashboard-stats")

urlpatterns = router.urls + [
    path("", DashboardView.as_view(), name="dashboard"),
]
