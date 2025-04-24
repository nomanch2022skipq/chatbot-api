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
