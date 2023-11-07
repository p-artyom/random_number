from django.contrib import admin

from core.admin import BaseAdmin
from number.models import AggregatedNumber, Number, NumberMoreNine


@admin.register(Number)
class NumberAdmin(BaseAdmin):
    '''Регистрация модели `Числа` в панели администратора.'''

    list_display = ('pk', 'time', 'value')


@admin.register(NumberMoreNine)
class NumberMoreNineAdmin(BaseAdmin):
    '''Регистрация модели `Числа более 9` в панели администратора.'''

    list_display = ('pk', 'time', 'value_more_nine')


@admin.register(AggregatedNumber)
class AggregatedNumberAdmin(BaseAdmin):
    '''Регистрация модели `Поминутно агрегированные числа` в админке.'''

    list_display = ('time_minute', 'avg_value')
