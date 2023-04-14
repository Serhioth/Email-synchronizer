from django.contrib import admin
from emails.models import LogPass


class LogPassAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'login',
                    'password',
                    'domain',
                    'password_yandex',
                    'email_yandex',
                    'fio',
                    'pub_date'
                    )
    list_editable = ('fio',)
    search_fields = ('login',)
    list_filter = ('pub_date', 'domain')
    empty_value_display = '-пусто-'


admin.site.register(LogPass, LogPassAdmin)
