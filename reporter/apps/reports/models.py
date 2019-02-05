from django.db import models


# Create your models here.
class Report(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    punish = models.DurationField(blank=False, null=False)
    reason = models.TextField(blank=False, null=False)
    timestamp = models.DateTimeField(blank=False, null=False, auto_now=True)
    reported_by = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return "{} at {} by {}".format(self.name, self.timestamp, self.punish, self.reported_by)
