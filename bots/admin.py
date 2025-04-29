from django.contrib import admin
from .models import BotsAgent


class BotsAgentAdmin(admin.ModelAdmin):
    list_display = (
        "agent_id",
        "agent_name",
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
    search_fields = ("agent_id", "agent_name", "website", "cid", "user__username")
    ordering = ("-started_date",)


admin.site.register(BotsAgent, BotsAgentAdmin)
