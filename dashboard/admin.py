from django.contrib import admin
from .models import DashboardStats


class DashboardStatsAdmin(admin.ModelAdmin):
    list_display = ("last_updated", "total_messages", "active_bots", "total_users")
    readonly_fields = ("last_updated",)


admin.site.register(DashboardStats, DashboardStatsAdmin)
