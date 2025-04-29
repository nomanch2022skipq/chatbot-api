from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Channel
from .serializers import ChannelSerializer


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(is_active=True)
        return queryset

    @action(detail=True, methods=["post"])
    def deactivate(self, request, pk=None):
        channel = self.get_object()
        channel.is_active = False
        channel.save()
        return Response({"status": "channel deactivated"})

    @action(detail=True, methods=["post"])
    def activate(self, request, pk=None):
        channel = self.get_object()
        channel.is_active = True
        channel.save()
        return Response({"status": "channel activated"})
