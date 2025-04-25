from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .models import *
from .serializers import *


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
    queryset = BotsAgent.objects.filter(is_deleted=False)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_superuser:
            return queryset
        return queryset.filter(user=user)

    @action(detail=True, methods=["post"])
    def share(self, request, pk=None):
        bot = self.get_object()
        serializer = BotShareSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(bot=bot)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["get"])
    def shared_users(self, request, pk=None):
        bot = self.get_object()
        shares = bot.shares.filter(is_active=True)
        serializer = BotShareSerializer(shares, many=True)
        return Response(serializer.data)


class BotsAgentViewMessages(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BotsAgentMessagesSerializer
    queryset = BotMessages.objects.all()
