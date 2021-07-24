from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import AbstractUser


# class Gender(models.Model):
#     gender = models.CharField(max_length=7)

class CustomUser(AbstractUser):
    
    age = models.PositiveIntegerField(null=True,blank=True)
    address = models.CharField(max_length=255,verbose_name='Address')
    # gender = models.ForeignKey(Gender,null=False,blank=False,on_delete=models.CASCADE)
