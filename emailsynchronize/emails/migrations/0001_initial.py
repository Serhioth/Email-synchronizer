# Generated by Django 4.1.7 on 2023-03-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogPass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(help_text='Новый логин', max_length=100, verbose_name='Логин пользователя')),
                ('password', models.CharField(help_text='Новый пароль пользователя', max_length=20, verbose_name='Новый пароль')),
                ('password_yandex', models.CharField(help_text='Пароль Яндекс', max_length=100, verbose_name='Пароль Яндекс')),
                ('email_yandex', models.EmailField(help_text='Эмейл Яндекс', max_length=254, verbose_name='Эмейл Яндекс')),
                ('domain', models.CharField(help_text='Старый домен', max_length=20, verbose_name='Домен пользователя')),
                ('fio', models.CharField(help_text='ФИО', max_length=100, verbose_name='ФИО пользователя')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Дата публикации', verbose_name='Дата публикации')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]
