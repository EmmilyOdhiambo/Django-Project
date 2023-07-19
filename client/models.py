from django.db import models

# Create your models here.

class Client(models.Model):
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    # date_of_birth = models.DateField(

    def register(self):
        self.save

    def get_client_by_email(email):
        try:
            return Client.objects.get(email=email)
        except:
            return False
        

    def isExist(self):
        if Client.objects.filter(email = self.email):
             return True
        
        return False
