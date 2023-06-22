from django.db import models

# Create your models here.

class Customerdata(models.Model):
    customer_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    order_history = models.TextField()
    payment_method = models.CharField(max_length=100)
    rating = models.IntegerField()
