# Generated by Django 5.2.4 on 2025-07-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0003_alter_flat_has_balcony"),
    ]

    operations = [
        migrations.AddField(
            model_name="flat",
            name="new_building",
            field=models.BooleanField(
                blank=True,
                db_index=True,
                help_text="True — новостройка, False — старое здание, None — не заполнено",
                null=True,
                verbose_name="Новостройка",
            ),
        ),
    ]
