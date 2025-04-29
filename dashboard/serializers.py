from rest_framework import serializers
from .models import DashboardStats


class DashboardStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardStats
        fields = ["id", "last_updated", "total_messages", "active_bots", "total_users"]
        read_only_fields = ["last_updated"]
