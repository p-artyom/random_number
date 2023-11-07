from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    '''Настройки панели администратора по умолчанию.'''

    empty_value_display = '-пусто-'
