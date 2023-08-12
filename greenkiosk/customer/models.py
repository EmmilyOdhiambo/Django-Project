from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    First_name= models.CharField(max_length=24)
    Last_name= models.CharField(max_length=30)
    Email_address= models.EmailField()
    Phone_number=models.CharField(max_length = 20)
    Password= models.CharField(max_length = 20)
    Password_comfirmation= models.CharField(max_length = 30)