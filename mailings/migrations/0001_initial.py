# Generated by Django 5.1 on 2024-08-14 14:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Введите Вашу электронную почту",
                        max_length=254,
                        verbose_name="email",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите Ваши ФИО", max_length=200, verbose_name="ФИО"
                    ),
                ),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="Комментарий"),
                ),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
            },
        ),
        migrations.CreateModel(
            name="Log",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_time_send",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата и время последней попытки"
                    ),
                ),
                (
                    "status",
                    models.CharField(max_length=50, verbose_name="Статус попытки"),
                ),
                (
                    "server_response",
                    models.TextField(
                        blank=True, null=True, verbose_name="Ответ сервера"
                    ),
                ),
            ],
            options={
                "verbose_name": "Лог",
                "verbose_name_plural": "Логи",
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subject",
                    models.CharField(
                        help_text="Укажите тему сообщения",
                        max_length=200,
                        verbose_name="тема письма",
                    ),
                ),
                (
                    "body",
                    models.TextField(
                        help_text="Заполните тело сообщения", verbose_name="Тело письма"
                    ),
                ),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
                "permissions": [("set_update", "Может менять сообщения")],
            },
        ),
        migrations.CreateModel(
            name="Newsletter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Напишите название рассылки",
                        max_length=200,
                        verbose_name=" Название рассылки",
                    ),
                ),
                (
                    "datetime_start",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Дата начала рассылки",
                    ),
                ),
                (
                    "datetime_send",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Дата отправки"
                    ),
                ),
                (
                    "datetime_finish",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Дата окончания рассылки",
                    ),
                ),
                (
                    "periodicity",
                    models.CharField(
                        choices=[
                            ("daily", "раз в день"),
                            ("weekly", "раз в неделю"),
                            ("monthly", "раз в месяц"),
                        ],
                        max_length=50,
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("completed", "Завершена"),
                            ("created", "Создана"),
                            ("launched", "Запущена"),
                        ],
                        default="created",
                        max_length=50,
                        verbose_name="Статус рассылки",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Актуальность"),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
                "permissions": [("set_is_active", "Может менять активность рассылки")],
            },
        ),
    ]
