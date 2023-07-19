from django.db import models

# Create your models here.
class Vendor(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()


