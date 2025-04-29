from django.contrib import admin
from .models import BotMessages

class BotMessagesAdmin(admin.ModelAdmin):
    list_display = ("conversation_id", "type", "agent", "channel", "created_at")
    list_filter = ("type", "created_at", "channel")
    search_fields = ("conversation_id", "message", "agent__agent_name")
    ordering = ("-created_at",)

admin.site.register(BotMessages, BotMessagesAdmin)
