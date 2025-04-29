from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import SharingCenter
from .serializers import SharingCenterSerializer


class SharingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SharingCenterSerializer

    def get_queryset(self):
        return SharingCenter.objects.filter(
            Q(primary_user=self.request.user) | Q(shared_user=self.request.user)
        )

    def perform_create(self, serializer):
        serializer.save(primary_user=self.request.user)

    @action(detail=False, methods=["get"])
    def shared_with_me(self, request):
        shares = self.get_queryset().filter(shared_user=request.user, is_active=True)
        serializer = self.get_serializer(shares, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def shared_by_me(self, request):
        shares = self.get_queryset().filter(primary_user=request.user)
        serializer = self.get_serializer(shares, many=True)
        return Response(serializer.data)
