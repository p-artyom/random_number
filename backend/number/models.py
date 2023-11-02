from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import TimestampedModel


class Number(TimestampedModel):
    value = models.FloatField(
        'число',
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
        ],
    )

    class Meta:
        verbose_name = 'число'
        verbose_name_plural = 'числа'
