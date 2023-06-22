from django.contrib import admin

# Register your models here.
from.models import Customerdata
class CustomerdataAdmin(admin.ModelAdmin):
    list_display=("customer_name","email_address","phone_number","address","order_history","payment_method","rating")
admin.site.register(Customerdata,CustomerdataAdmin)
