from django.db import models


class WorshipSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    info = models.JSONField()
