from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import BotMessages
from .serializers import BotMessagesSerializer

class MessagesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BotMessagesSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return BotMessages.objects.all()
        return BotMessages.objects.filter(
            Q(agent__user=user) | 
            Q(agent__sharing_records__shared_user=user, agent__sharing_records__is_active=True)
        ).distinct()
