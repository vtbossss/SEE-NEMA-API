# Generated by Django 4.2.16 on 2024-10-10 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="watchlist",
            name="user",
        ),
    ]
