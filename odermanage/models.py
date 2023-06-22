from django.db import models

# Create your models here.

class Odermanage(models.Model):
    order_id = models.IntegerField()
    customer_id = models.IntegerField()
    vendor_id = models.IntegerField()
    order_date = models.DateField()
    order_status = models.CharField(max_length=50)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_items = models.TextField()
