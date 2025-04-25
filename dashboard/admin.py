from django.contrib import admin
from .models import BotMessages, BotsAgent, BotChannels


class BotChannelsAdmin(admin.ModelAdmin):
    list_display = ("channel_name", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("channel_name",)
    ordering = ("-created_at",)


class BotsAgentAdmin(admin.ModelAdmin):
    list_display = (
        "agent_id",
        "user",
        "website",
        "is_active_subscription",
        "is_direct_start",
        "started_date",
        "is_deleted",
    )
    list_filter = (
        "is_active_subscription",
        "is_direct_start",
        "is_deleted",
    )
    search_fields = ("agent_id", "website", "cid", "user__username")
    ordering = ("-started_date",)

class BotMessagesAdmin(admin.ModelAdmin):
    list_display = ("conversation_id", "message", "channel", "type", "created_at")
    list_filter = ("type", "created_at")
    search_fields = ("conversation_id", "message", "channel__channel_name")
    ordering = ("-created_at",)

admin.site.register(BotsAgent, BotsAgentAdmin)
admin.site.register(BotChannels, BotChannelsAdmin)
admin.site.register(BotMessages, BotMessagesAdmin)
