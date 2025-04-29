from rest_framework import serializers
from .models import SharingCenter
from django.contrib.auth import get_user_model

User = get_user_model()


class SharingCenterSerializer(serializers.ModelSerializer):
    primary_user_username = serializers.CharField(
        source="primary_user.username", read_only=True
    )
    shared_user_username = serializers.CharField(
        source="shared_user.username", read_only=True
    )
    bot_name = serializers.CharField(source="bot.agent_name", read_only=True)

    class Meta:
        model = SharingCenter
        fields = [
            "id",
            "primary_user",
            "shared_user",
            "bot",
            "primary_user_username",
            "shared_user_username",
            "bot_name",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def validate(self, attrs):
        if attrs.get("primary_user") == attrs.get("shared_user"):
            raise serializers.ValidationError("Cannot share a bot with yourself")

        # Check if the sharing relationship already exists
        if SharingCenter.objects.filter(
            primary_user=attrs.get("primary_user"),
            shared_user=attrs.get("shared_user"),
            bot=attrs.get("bot"),
        ).exists():
            raise serializers.ValidationError(
                "This bot is already shared with this user"
            )

        return attrs
