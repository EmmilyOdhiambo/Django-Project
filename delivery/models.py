from django.db import models

# Create your models here.


class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    contact_number = models.CharField(max_length=20)
    delivery_date = models.DateField()
    time = models.TimeField()
    cyclist_name = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    

