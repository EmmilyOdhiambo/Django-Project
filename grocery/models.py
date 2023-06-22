from django.db import models

# Create your models here.

class Grocery(models.Model):
    product_id = models.IntegerField()
    grocery_name = models.CharField(max_length=100)
    description = models.TextField()
    expiry_date = models.DateField()
    stocked_date = models.DateField()
    brand = models.CharField(max_length=50)
    quantity = models.IntegerField()
