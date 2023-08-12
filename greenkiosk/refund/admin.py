from django.contrib import admin

# Register your models here.
from .models import Refund

class  RefundAdmin(admin.ModelAdmin):
    list=("name","date","price_name")
admin.site. register(Refund,RefundAdmin) 
