from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.CharField(max_length=100)
    grocery_name = models.CharField(max_length=200)
    description = models.TextField()
    expiry_date = models.DateField()
    stocked_date = models.DateField()
    brand = models.CharField(max_length=100)
    quantity = models.IntegerField()
  
