from django.contrib import admin

# Register your models here.
from.models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display=("payment_id","payment_method","amount","currency","date","status","customer_id")
admin.site.register(Payment,PaymentAdmin)

