from django.db import models


class DefaultModel(models.Model):
    class Meta:
        abstract = True


class TimestampedModel(DefaultModel):
    time = models.DateTimeField('дата создания', auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ('-time',)
