# Generated by Django 5.0 on 2024-04-12 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRN', '0004_import_pr_import_pr_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_orders',
            name='remaining',
            field=models.FloatField(blank=True, null=True),
        ),
    ]