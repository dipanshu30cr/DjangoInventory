from django.db import models

from user.models import *
import uuid
from django.utils import timezone


class Item(models.Model):
    ItemId = models.AutoField(primary_key=True)
    ItemName = models.CharField(max_length=30, unique=True)
    ItemRate = models.IntegerField(null=False, blank=False)
    Itemstatus = models.IntegerField(default=1)  
    ItemEntryDate = models.DateField(default=timezone.now)
    UserId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        db_table = 'tbl_item_mstr'

    