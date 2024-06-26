# Generated by Django 5.0 on 2024-02-29 08:30

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRN', '0002_pr_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='GRN',
            fields=[
                ('GRN_no', models.TextField(primary_key=True, serialize=False)),
                ('grn_date', models.DateField(blank=True, null=True)),
                ('recieved_from', models.TextField(blank=True, null=True)),
                ('transporter_name', models.TextField(blank=True, null=True)),
                ('truck_no', models.TextField(blank=True, null=True)),
                ('store_name', models.TextField(blank=True, null=True)),
                ('store_keeper', models.TextField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('PR_no', models.ForeignKey(blank=True, db_column='PR_no', null=True, on_delete=django.db.models.deletion.CASCADE, to='GRN.purchase_orders')),
            ],
        ),
        migrations.CreateModel(
            name='GRN_item',
            fields=[
                ('grn_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('item_name', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
                ('GRN_no', models.ForeignKey(db_column='GRN_no', on_delete=django.db.models.deletion.CASCADE, to='GRN.grn')),
                ('PR_no', models.ForeignKey(db_column='PR_no', on_delete=django.db.models.deletion.CASCADE, to='GRN.purchase_orders')),
            ],
        ),
    ]
