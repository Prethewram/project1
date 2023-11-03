from django.db import models

# Create your models here.


class registerdb1(models.Model):
    Name = models.CharField(max_length=20,blank=True,null=True)
    Mobile = models.IntegerField(blank=True,null=True)
    Email = models.EmailField(max_length=50,blank=True,null=True)
    Address = models.CharField(max_length=100,blank=True,null=True)
    Username = models.CharField(max_length=50,blank=True,null=True)
    Password = models.CharField(max_length=50,blank=True,null=True)


class cartdb(models.Model):
    Username = models.CharField(max_length=20,blank=True,null=True)
    Productname = models.CharField(max_length=20,blank=True,null=True)
    Description = models.CharField(max_length=20,blank=True,null=True)
    Quantity = models.IntegerField(blank=True,null=True)
    Totalprize = models.IntegerField(blank=True,null=True)