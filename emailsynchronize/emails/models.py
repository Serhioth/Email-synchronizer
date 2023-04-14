from django.db import models


class LogPass(models.Model):
    login = models.CharField(
        'Логин пользователя',
        max_length=100,
        help_text='Новый логин'
    )
    password = models.CharField(
        'Новый пароль',
        max_length=20,
        help_text='Новый пароль пользователя'
    )
    portal_password = models.CharField(
        'Пароль от почты пользователя',
        max_length=100,
        help_text='Пароль от почты пользователя'
    )
    user_email = models.EmailField(
        'Эмейл пользователя',
        help_text='Эмейл пользователя'
    )
    domain = models.CharField(
        'Домен пользователя',
        max_length=20,
        help_text='Старый домен'
    )

    fio = models.CharField(
        'ФИО пользователя',
        max_length=100,
        help_text='ФИО'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True,
        help_text='Дата публикации'
    )

    class Meta:
        ordering = ('-pub_date',)
