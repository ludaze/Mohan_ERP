# Generated by Django 5.0 on 2024-02-29 08:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRN', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PR_item',
            fields=[
                ('id_numeric', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('before_vat', models.FloatField(blank=True, null=True)),
                ('total_price', models.FloatField(blank=True, null=True)),
                ('quantity', models.FloatField()),
                ('remaining', models.FloatField()),
                ('item_measurement', models.TextField(blank=True, null=True)),
                ('PR_no', models.ForeignKey(blank=True, db_column='PR_no', null=True, on_delete=django.db.models.deletion.CASCADE, to='GRN.purchase_orders')),
            ],
        ),
    ]
