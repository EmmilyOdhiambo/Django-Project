from django.contrib import admin

# Register your models here.
from.models import Odermanage
class OdermanageAdmin(admin.ModelAdmin):
    list_display=("order_id","customer_id","vendor_id","order_date","order_status","order_total","order_items")
admin.site.register(Odermanage,OdermanageAdmin)
