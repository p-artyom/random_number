from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import TimestampedModel


class Number(TimestampedModel):
    '''Модель `Числа`.'''

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


class NumberMoreNine(TimestampedModel):
    '''Модель `Числа более 9`.'''

    value_more_nine = models.FloatField(
        'число больше 9',
        validators=[
            MaxValueValidator(10),
            MinValueValidator(9),
        ],
    )

    class Meta:
        verbose_name = 'число больше 9'
        verbose_name_plural = 'числа больше 9'


class AggregatedNumber(models.Model):
    '''Представление данных `Поминутно агрегированные числа`.'''

    time_minute = models.DateTimeField('дата создания', primary_key=True)
    avg_value = models.FloatField(
        'агрегированное число',
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
        ],
    )

    class Meta:
        managed = False
        db_table = 'minute_by_minute_aggregated_data'
        verbose_name = 'агрегированное число'
        verbose_name_plural = 'агрегированные числа'
