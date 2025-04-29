from rest_framework import serializers
from .models import BotsAgent
from channels.models import Channel
from channels.serializers import ChannelSerializer


class BotsAgentSerializer(serializers.ModelSerializer):
    channels = ChannelSerializer(many=True, read_only=True)
    channel_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        source="channels",
        queryset=Channel.objects.filter(is_active=True),
    )

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
            "channels",
            "channel_ids",
            "fine_tune_stage",
            "custom_persona",
            "is_deleted",
        ]
        read_only_fields = ["agent_id", "started_date"]
