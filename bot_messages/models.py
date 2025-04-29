from django.db import models
from bots.models import BotsAgent
from channels.models import Channel


class BotMessages(models.Model):
    conversation_id = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    channel = models.ForeignKey(
        Channel, on_delete=models.CASCADE, related_name="channel_messages"
    )
    type = models.CharField(
        max_length=50, choices=[("incoming", "Incoming"), ("outgoing", "Outgoing")]
    )
    agent = models.ForeignKey(
        BotsAgent,
        on_delete=models.CASCADE,
        related_name="agent_messages",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Message from {self.agent_id} at {self.created_at}"

    class Meta:
        verbose_name = "Bot Message"
        verbose_name_plural = "Bot Messages"
        ordering = ["-created_at"]
