from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from bot_messages.models import BotMessages
from bots.models import BotsAgent
from .models import DashboardStats
from .serializers import DashboardStatsSerializer

User = get_user_model()


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get latest stats or create new
        stats, created = DashboardStats.objects.get_or_create(pk=1)

        # Update stats
        stats.total_messages = BotMessages.objects.count()
        stats.active_bots = BotsAgent.objects.filter(is_deleted=False).count()
        stats.total_users = User.objects.filter(is_active=True).count()
        stats.save()

        serializer = DashboardStatsSerializer(stats)
        return Response(serializer.data)


class DashboardStatsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = DashboardStats.objects.all()
    serializer_class = DashboardStatsSerializer
