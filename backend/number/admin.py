from django.contrib import admin

from core.admin import BaseAdmin
from number.models import Number, NumberMoreNine


@admin.register(Number)
class NumberAdmin(BaseAdmin):
    list_display = ('pk', 'time', 'value')


@admin.register(NumberMoreNine)
class NumberMoreNineAdmin(BaseAdmin):
    list_display = ('pk', 'time')
