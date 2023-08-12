from django.contrib import admin

# Register your models here.
from .models import Vendor
class Vendor_admin(admin.ModelAdmin):
    list_display=("First_name","Last_name","Email_address","Phone_number","Password","Password_comfirmation")
 
admin.site.register(Vendor, Vendor_admin)
