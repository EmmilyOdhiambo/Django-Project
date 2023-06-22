from django.contrib import admin

# Register your models here.
from.models import Delivery
class DeliveryAdmin(admin.ModelAdmin):
    list_display=("id","contact_number","delivery_date","time","cyclist_name","delivery_address","status")
admin.site.register(Delivery,DeliveryAdmin)