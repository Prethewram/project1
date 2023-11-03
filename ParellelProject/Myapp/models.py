from django.db import models

# Create your models here.

class shopdb(models.Model):
    CName = models.CharField(max_length=100,null=True,blank=True)
    CDes = models.CharField(max_length=100,null=True,blank=True)
    Cimage = models.ImageField(upload_to="profile",null=True,blank=True)

class productdb(models.Model):
     Catname = models.CharField(max_length=100,null=True,blank=True)
     Productname = models.CharField(max_length=100,null=True,blank=True)
     Description = models.CharField(max_length=100,null=True,blank=True)
     Price = models.IntegerField(null=True,blank=True)
     Image = models.ImageField(upload_to="profile",null=True,blank=True)


class contactdb(models.Model):
    Firstname = models.CharField(max_length=100,null=True,blank=True)
    Lastname = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Address = models.EmailField(max_length=100,null=True,blank=True)
    City = models.EmailField(max_length=100,null=True,blank=True)
    Zipcode = models.IntegerField(null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
