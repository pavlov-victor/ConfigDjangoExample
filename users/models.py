from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    middle_name = models.CharField("Отчество", max_length=100)
    birth_date = models.DateField("Дата рождения", default=None, null=True, blank=True)
    phone = models.IntegerField(
        "Номер телефона", max_length=15, default=None, null=True
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
