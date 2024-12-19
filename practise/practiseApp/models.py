from django.db import models

# Create your models here.

class Register(models.Model):
    Full_Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Phone_Number=models.IntegerField()
    Course=models.CharField(max_length=50)