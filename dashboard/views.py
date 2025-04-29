from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .models import DashboardStats
from .serializers import DashboardStatsSerializer

User = get_user_model()

class DashboardStatsViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "put"]
    permission_classes = [IsAuthenticated]
    queryset = DashboardStats.objects.filter(pk=1)
    serializer_class = DashboardStatsSerializer
