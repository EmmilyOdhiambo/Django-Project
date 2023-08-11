from django.contrib import admin


# Register your models here.

from.models import Vendor
class VendorAdmin(admin.ModelAdmin):
    list_display = ("email", "password", "first_name", "last_name", "phone_number", "date_of_birth")
admin.site.register(Vendor,VendorAdmin)



