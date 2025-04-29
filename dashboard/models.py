from django.db import models


class DashboardStats(models.Model):
    last_updated = models.DateTimeField(auto_now=True)
    total_messages = models.IntegerField(default=0)
    active_bots = models.IntegerField(default=0)
    total_users = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Dashboard Statistic"
        verbose_name_plural = "Dashboard Statistics"

    def __str__(self):
        return f"Dashboard Stats (Updated: {self.last_updated})"
