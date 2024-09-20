from django.db import models
from django.utils import timezone
from inventory.models import *
from purchase.models import *

# Create your models here.
class SalesMaster(models.Model):
    SalesMasterId= models.AutoField(primary_key=True)
    CustomerName=models.CharField(max_length=30)
    CustomerPhone=models.CharField(max_length=30)
    SalesMasterReference=models.CharField(max_length=30, unique=True)
    SalesDate=models.DateField(null=True, blank=True)
    SalesMasterEntryDate = models.DateField(default=timezone.now)
    SalesMasterTotal= models.CharField(max_length=30)
    SalesMasterstatus = models.IntegerField(default=1) 

    class Meta:
        db_table = 'tbl_sales_mstr'


class SalesDetails(models.Model):
    SalesDetailId=models.AutoField(primary_key=True)
    ItemAssigned = models.ForeignKey(Item, on_delete=models.CASCADE)
    ItemQuantity= models.IntegerField()
    ItemPrice= models.IntegerField()
    ItemAmount= models.CharField()
    SalesMasterId= models.ForeignKey(SalesMaster , on_delete=models.CASCADE)
    SalesDetailEntryDate=models.DateField(default=timezone.now)
    SalesDetailsstatus = models.IntegerField(default=1) 


    class Meta:
        db_table= 'tbl_sales_dtl'


# class SalesDetails(models.Model):
#     SalesDetailId=models.AutoField(primary_key=True)
#     ItemAssigned = models.ForeignKey(PurchaseDetails, on_delete=models.CASCADE)
#     ItemQuantity= models.IntegerField()
#     ItemPrice= models.IntegerField()
#     ItemAmount= models.CharField()
#     SalesMasterId= models.ForeignKey(SalesMaster , on_delete=models.CASCADE)
#     SalesDetailEntryDate=models.DateField(default=timezone.now)
#     SalesDetailsstatus = models.IntegerField(default=1) 


#     class Meta:
#         db_table= 'tbl_sales_dtl'
