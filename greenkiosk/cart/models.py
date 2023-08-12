from django.db import models
from inventory.models import Product
# Create your models here.
class Cart(models.Model):
    products = models.ManyToManyField(Product)
    name  = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    quantity = models.PositiveIntegerField()

