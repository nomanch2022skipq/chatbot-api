from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import BotChannels, BotsAgent
from .serializers import BotChannelsSerializer, BotsAgentSerializer


class DashboardView(APIView):
    def get(self, request):
        return Response({"message": "Dashboard"})


class BotChannelsViewSet(viewsets.ModelViewSet):
    queryset = BotChannels.objects.all()
    serializer_class = BotChannelsSerializer
    permission_classes = [IsAuthenticated]


class BotsAgentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BotsAgentSerializer

    def get_queryset(self):
        return BotsAgent.objects.filter(is_deleted=False)
