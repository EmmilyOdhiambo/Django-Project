from django.contrib import admin

# Register your models here.

from.models import Grocery
class GroceryAdmin(admin.ModelAdmin):
    list_display=("product_id","grocery_name","description","expiry_date","stocked_date","brand","quantity")
admin.site.register(Grocery,GroceryAdmin)
