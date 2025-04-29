from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import BotsAgent
from .serializers import BotsAgentSerializer


class BotsAgentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BotsAgentSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return BotsAgent.objects.filter(is_deleted=False)
        return BotsAgent.objects.filter(
            Q(user=user)
            | Q(sharing_records__shared_user=user, sharing_records__is_active=True),
            is_deleted=False,
        ).distinct()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["post"])
    def archive(self, request, pk=None):
        bot = self.get_object()
        if bot.user != request.user:
            return Response(
                {"error": "You don't have permission to archive this bot"},
                status=status.HTTP_403_FORBIDDEN,
            )
        bot.is_deleted = True
        bot.save()
        return Response({"message": "Bot archived successfully"})
