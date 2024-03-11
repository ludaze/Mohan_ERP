# Generated by Django 5.0 on 2024-02-29 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='purchase_orders',
            fields=[
                ('vendor_name', models.TextField(blank=True, null=True)),
                ('PR_no', models.TextField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('site_name', models.TextField()),
                ('payment_type', models.TextField(blank=True, null=True)),
                ('requested_by', models.TextField(blank=True, null=True)),
                ('approved_by', models.TextField(blank=True, null=True)),
                ('PR_total_price', models.FloatField(blank=True, null=True)),
                ('PR_before_vat', models.FloatField(blank=True, null=True)),
                ('status', models.TextField(blank=True, default='Pending', null=True)),
                ('total_quantity', models.FloatField(blank=True, null=True)),
                ('measurement_type', models.TextField(blank=True, null=True)),
            ],
        ),
    ]