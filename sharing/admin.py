from django.contrib import admin
from .models import SharingCenter


class SharingCenterAdmin(admin.ModelAdmin):
    list_display = (
        "primary_user",
        "shared_user",
        "bot",
        "is_active",
        "created_at",
    )
    list_filter = ("is_active", "created_at")
    search_fields = (
        "primary_user__username",
        "shared_user__username",
        "bot__agent_name",
    )
    ordering = ("-created_at",)


admin.site.register(SharingCenter, SharingCenterAdmin)
