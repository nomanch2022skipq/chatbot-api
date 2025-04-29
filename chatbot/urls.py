from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from authentication.views import CustomLoginView, CustomLogoutView

schema_view = get_schema_view(
    openapi.Info(
        title="Chatbot API",
        default_version="v1",
        description="API documentation for Chatbot project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/dashboard/", include("dashboard.urls")),
    path("api/auth/", include("authentication.urls")),
    path("api/bots/", include("bots.urls")),
    path("api/messages/", include("bot_messages.urls")),
    path("api/sharing/", include("sharing.urls")),
    path("api/channels/", include("channels.urls")),
    path("api-auth/", include("rest_framework.urls")),  # DRF's built-in auth views
    path("accounts/login/", CustomLoginView.as_view(), name="login"),
    path("accounts/logout/", CustomLogoutView.as_view(), name="logout"),
    # Swagger URLs
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
]
