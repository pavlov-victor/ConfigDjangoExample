# Generated by Django 4.1.1 on 2022-09-06 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.IntegerField(
                default=None, max_length=15, null=True, verbose_name="Номер телефона"
            ),
        ),
    ]
