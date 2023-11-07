from django.db import models


class DefaultModel(models.Model):
    '''Модель по умолчанию.'''

    class Meta:
        abstract = True


class TimestampedModel(DefaultModel):
    '''Модель с временной меткой.'''

    time = models.DateTimeField('дата создания', auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ('-time',)
