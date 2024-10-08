# Generated by Django 5.1.1 on 2024-09-09 12:40

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0003_alter_item_itemstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseMaster',
            fields=[
                ('PurchaseMasterId', models.AutoField(primary_key=True, serialize=False)),
                ('PurchaseMasterReference', models.CharField(max_length=30)),
                ('PurchaseMasterTotal', models.CharField(max_length=30)),
                ('PurchaseMasterEntryDate', models.DateField(default=django.utils.timezone.now)),
                ('PurchaseMasterDate', models.DateField(default=django.utils.timezone.now)),
                ('PurchaseMasterstatus', models.IntegerField(default=1)),
                ('UserId', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
            options={
                'db_table': 'tbl_purchase_mstr',
            },
        ),
        migrations.CreateModel(
            name='PurchaseDetails',
            fields=[
                ('PurchaseDetailsId', models.AutoField(primary_key=True, serialize=False)),
                ('Quantity', models.IntegerField()),
                ('Amount', models.CharField()),
                ('PurchaseDetailsEntryDate', models.DateField(default=django.utils.timezone.now)),
                ('PurchaseDetailsstatus', models.IntegerField(default=1)),
                ('UserId', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('ItemAssigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
                ('PurchaseMasterAssigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.purchasemaster')),
            ],
            options={
                'db_table': 'tbl_purchase_dtl',
            },
        ),
    ]
