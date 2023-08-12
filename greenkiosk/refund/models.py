from django.db import models

# Create your models here.
class Refund(models.Model):
    name=models.CharField(max_length=20)
    date=models.DateTimeField
    price_name=models.DecimalField(max_digits=4,decimal_places=2)
    
