from django.db import models
from inventory.models import *
# Create your models here.
class Report(models.Model):
    Quantity= models.ForeignKey(Item, on_delete=models.CASCADE)
    
