from rest_framework import serializers
from .models import BotMessages

class BotMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotMessages
        fields = '__all__'