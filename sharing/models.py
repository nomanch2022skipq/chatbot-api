from django.db import models
from django.conf import settings
from bots.models import BotsAgent


class SharingCenter(models.Model):
    primary_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sharing_by_me"
    )
    shared_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sharing_with_me",
    )
    bot = models.ForeignKey(
        BotsAgent, on_delete=models.CASCADE, related_name="bot_sharing_records"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Sharing Center"
        verbose_name_plural = "Sharing Centers"
        unique_together = ("primary_user", "shared_user", "bot")

    def __str__(self):
        return f"{self.primary_user.username} shared {self.bot.agent_name} with {self.shared_user.username}"
