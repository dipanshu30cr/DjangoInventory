from django.db import models

# Create your models here.
class Teacher(models.Model):
    TeacherId= models.AutoField(primary_key=True)
    TeacherName= models.CharField(max_length=30 )
    Subject= models.CharField(max_length=30 )
