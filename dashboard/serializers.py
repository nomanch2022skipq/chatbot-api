from rest_framework import serializers
from .models import BotChannels, BotsAgent


class BotChannelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotChannels
        fields = ["id", "channel_name", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


class BotsAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotsAgent
        fields = [
            "id",
            "agent_id",
            "agent_name",
            "started_date",
            "is_active_subscription",
            "is_direct_start",
            "cancellation_date",
            "website",
            "cid",
            "scrape_status",
            "welcome_message",
            "logo",
            "user",
            "fine_tune_stage",
            "custom_persona",
            "is_deleted",
        ]
        read_only_fields = ["agent_id", "started_date"]
