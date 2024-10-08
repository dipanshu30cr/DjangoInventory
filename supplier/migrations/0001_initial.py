# Generated by Django 5.1.1 on 2024-09-09 10:28

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('SupplierId', models.AutoField(primary_key=True, serialize=False)),
                ('SupplierName', models.CharField(max_length=30)),
                ('SupplierAddress', models.CharField(max_length=30)),
                ('SupplierContact', models.CharField(max_length=30, unique=True)),
                ('Supplierstatus', models.IntegerField(default=1)),
                ('SupplierEntryDate', models.DateField(default=django.utils.timezone.now)),
                ('UserId', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
            options={
                'db_table': 'tbl_supplier_mstr',
            },
        ),
    ]
