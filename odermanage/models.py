from django.db import models
from client.models import Client
from Add_to_cart.models import Add_to_cart
from delivery.models import Delivery

class Odermanage(models.Model):
    name = models.CharField(max_length=32, default='Default Name')  # Add a default value
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=8, decimal_places=3, default=0.0)
    # image = models.ImageField()
    # description = models.TextField()

    client = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)
    Add_to_cart = models.ForeignKey(Add_to_cart, null=True, on_delete=models.CASCADE)
    delivery = models.OneToOneField(Delivery, null=True, on_delete=models.CASCADE)
