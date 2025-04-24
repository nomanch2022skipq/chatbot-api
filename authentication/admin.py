from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "subscription_plan",
        "is_deleted",
        "is_staff",
    )
    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        "subscription_plan",
        "is_deleted",
    )
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)


admin.site.register(User, CustomUserAdmin)
