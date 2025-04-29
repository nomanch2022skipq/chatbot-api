from django.contrib import admin
from .models import Channel


class ChannelAdmin(admin.ModelAdmin):
    list_display = (
        "channel_name",
        "description",
        "is_active",
        "created_at",
        "updated_at",
    )
    list_filter = ("is_active", "created_at")
    search_fields = ("channel_name", "description")
    ordering = ("-created_at",)


admin.site.register(Channel, ChannelAdmin)
