# Generated by Django 5.1.1 on 2024-09-11 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_item_itemstatus'),
        ('sales', '0003_alter_salesdetails_itemassigned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesdetails',
            name='ItemAssigned',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item'),
        ),
    ]
