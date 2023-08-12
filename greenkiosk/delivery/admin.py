from django.contrib import admin

# Register your models here.
from .models import Delivery

class DeliveryAdmin(admin.ModelAdmin):
    list_display= ("recipient_name","recipient_phone","delivery_address","delivery_date","delivery_status")

admin.site.register(Delivery,DeliveryAdmin)
