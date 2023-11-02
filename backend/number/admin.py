from django.contrib import admin

from core.admin import BaseAdmin
from number.models import Number


@admin.register(Number)
class CategoryAdmin(BaseAdmin):
    list_display = ('pk', 'time', 'value')
