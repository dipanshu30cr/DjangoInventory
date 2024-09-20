from django.db import models

import uuid
from django.utils import timezone


class Supplier(models.Model):
    SupplierId = models.AutoField(primary_key=True)
    SupplierName = models.CharField(max_length=30)
    SupplierAddress = models.CharField(max_length=30)
    SupplierContact = models.CharField(max_length=30, unique=True)
    Supplierstatus = models.IntegerField(default=1)  
    SupplierEntryDate = models.DateField(default=timezone.now)
    UserId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        db_table = 'tbl_supplier_mstr'

    