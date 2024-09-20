from django.db import models
import uuid
from django.utils import timezone
from inventory.models import *
from supplier .models import *



class PurchaseMaster(models.Model):
    PurchaseMasterId = models.AutoField(primary_key=True)
    PurchaseMasterReference = models.CharField(max_length=30)
    PurchaseMasterTotal = models.CharField(max_length=30)
    PurchaseMasterEntryDate = models.DateField(default=timezone.now)
    PurchaseMasterDate = models.DateField(default=timezone.now)
    PurchaseSupplier= models.ForeignKey(Supplier, on_delete=models.CASCADE, default=1)
    PurchaseMasterstatus = models.IntegerField(default=1)  
    
    #UserId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        db_table = 'tbl_purchase_mstr'


class PurchaseDetails(models.Model):
    PurchaseDetailsId = models.AutoField(primary_key=True)
    PurchaseMasterAssigned = models.ForeignKey(PurchaseMaster, on_delete=models.CASCADE)
    ItemAssigned = models.ForeignKey(Item, on_delete=models.CASCADE)
    Quantity= models.IntegerField()
    Amount= models.CharField()
    PurchaseDetailsEntryDate = models.DateField(default=timezone.now)
    
    PurchaseDetailsstatus = models.IntegerField(default=1)  

    class Meta:
        db_table = 'tbl_purchase_dtl'

    