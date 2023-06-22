from django.db import models

# Create your models here.

class Shoppingcart(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_quantity = models.IntegerField()
    product_image = models.ImageField(upload_to='product_images/')
    vendor_id = models.IntegerField()
    date_added = models.DateField()
