from django.db import models

# Create your models here.

class Stock(models.Model):
    store_name = models.CharField(max_length=100)
    store_location = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_information = models.CharField(max_length=100)
    email = models.EmailField()
