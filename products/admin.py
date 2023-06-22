from django.contrib import admin

# Register your models here.
from.models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display=("id","product_id","grocery_name","description","expiry_date","stocked_date","brand","quantity")
admin.site.register(Product,ProductAdmin)
