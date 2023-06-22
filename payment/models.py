from django.db import models

# Create your models here.

class Payment(models.Model):
    payment_id = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    date = models.DateField()
    status = models.CharField(max_length=50)
    customer_id = models.IntegerField()