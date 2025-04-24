from django.contrib import admin
from .models import BotsAgent, BotChannels


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


admin.site.register(BotsAgent, BotsAgentAdmin)
admin.site.register(BotChannels, BotChannelsAdmin)
