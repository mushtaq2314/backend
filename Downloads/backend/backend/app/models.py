from django.db import models

# Create your models here.
class orders(models.Model):
    username = models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    size = models.CharField(max_length=1000)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    method = models.CharField(max_length=255)
class customizations(models.Model):
    username = models.CharField(max_length=255)
    occasion = models.CharField(max_length=255)
    pricerange = models.CharField(max_length=255)
    skintone = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=1000)
    #
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    method = models.CharField(max_length=255)    