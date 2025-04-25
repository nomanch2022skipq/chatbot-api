from rest_framework import serializers
from .models import BotChannels, BotMessages, BotsAgent, BotShare


class BotChannelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotChannels
        fields = ["id", "channel_name", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


class BotShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotShare
        fields = ["id", "bot", "shared_with", "is_active", "created_at"]
        read_only_fields = ["shared_by", "created_at"]

    def create(self, validated_data):
        validated_data["shared_by"] = self.context["request"].user
        return super().create(validated_data)


class BotsAgentSerializer(serializers.ModelSerializer):
    shared_with = serializers.SerializerMethodField()

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
            "shared_with",
        ]
        read_only_fields = ["agent_id", "started_date"]

    def get_shared_with(self, obj):
        shares = obj.shares.filter(is_active=True).values_list("shared_with", flat=True)
        return list(shares)


class BotsAgentMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotMessages
        fields = "__all__"
