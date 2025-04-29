from django.db import models


class Channel(models.Model):
    channel_name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.channel_name

    class Meta:
        verbose_name = "Channel"
        verbose_name_plural = "Channels"
        ordering = ["-created_at"]
