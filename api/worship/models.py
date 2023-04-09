from django.db import models

class Schedule(models.Model):
    info = models.JSONField()

    def __str__(self):
        return f"Schedule {self.id}: {self.info}"