from django.db import models

# Create your models here.
class Delivery(models.Model):
    recipient_name= models.CharField(max_length=20)
    recipient_phone= models.CharField(max_length=20)
    delivery_address= models.CharField(max_length=100)
    delivery_date= models.DateTimeField()
    delivery_status= models.CharField(max_length=34)
    