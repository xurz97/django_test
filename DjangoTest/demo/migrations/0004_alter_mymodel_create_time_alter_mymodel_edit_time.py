# Generated by Django 4.2.6 on 2023-10-26 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("demo", "0003_remove_mymodel_number1_remove_mymodel_number2_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mymodel",
            name="create_time",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="mymodel",
            name="edit_time",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
