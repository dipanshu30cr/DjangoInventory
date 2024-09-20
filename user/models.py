
from django.db import models
from django.utils import timezone

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    userName = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    entryDate = models.DateField(default=timezone.now)
    userStatus = models.IntegerField(default=1)

    class Meta:
        db_table = 'tbl_user'

class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(default=timezone.now)
    logout_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'tbl_session'
