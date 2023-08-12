from django.db import models

# Create your models here.
class Signup(models.Model):
    Email_address= models.EmailField()
    Phone_number= models.BigIntegerField()
    Password= models.CharField(max_length = 20)
    Password_comfirmation= models.CharField(max_length = 30)