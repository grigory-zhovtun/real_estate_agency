# Generated by Django 5.2.4 on 2025-07-10 10:38

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0009_alter_flat_liked_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="flat",
            name="owner_pure_phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                help_text="Введите номер телефона в формате +7XXXXXXXXXX",
                max_length=128,
                region=None,
                verbose_name="Нормализованный номер владельца",
            ),
        ),
    ]
