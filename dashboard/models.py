from django.db import models
from django.conf import settings
import uuid


class BotChannels(models.Model):
    channel_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.channel_name

    class Meta:
        verbose_name = "Bot Channel"
        verbose_name_plural = "Bot Channels"


class BotsAgent(models.Model):
    agent_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    agent_name = models.CharField(max_length=255, null=True, blank=True)
    started_date = models.DateTimeField(auto_now_add=True)
    is_active_subscription = models.BooleanField(default=False)
    is_direct_start = models.BooleanField(default=False)
    cancellation_date = models.DateTimeField(null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    cid = models.CharField(max_length=255, null=True, blank=True)
    scrape_status = models.CharField(max_length=255, null=True, blank=True)
    welcome_message = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to="bots_logo/", null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    fine_tune_stage = models.IntegerField(default=0)
    custom_persona = models.CharField(max_length=255, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.agent_id)

    class Meta:
        verbose_name = "Bot Agent"
        verbose_name_plural = "Bot Agents"


class BotMessages(models.Model):
    conversation_id = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    channel = models.ForeignKey(
        BotChannels, on_delete=models.CASCADE, related_name="messages"
    )
    type = models.CharField(
        max_length=50, choices=[("incoming", "Incoming"), ("outgoing", "Outgoing")]
    )
    agent = models.ForeignKey(
        BotsAgent,
        on_delete=models.CASCADE,
        related_name="messages",
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


class BotShare(models.Model):
    bot = models.ForeignKey(BotsAgent, on_delete=models.CASCADE, related_name="shares")
    shared_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="shared_bots"
    )
    shared_with = models.EmailField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.bot.agent_name} shared with {self.shared_with}"

    class Meta:
        verbose_name = "Bot Share"
        verbose_name_plural = "Bot Shares"
        unique_together = ("bot", "shared_with")
