# Generated by Django 5.0 on 2024-04-12 07:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("FGRN", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="fgrn",
            name="recieved_BY",
            field=models.TextField(blank=True, null=True),
        ),
    ]