# Generated by Django 4.2.6 on 2023-10-26 10:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("demo", "0004_alter_mymodel_create_time_alter_mymodel_edit_time"),
    ]

    operations = [
        migrations.DeleteModel(
            name="TestModel",
        ),
    ]
