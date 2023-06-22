from django.contrib import admin

# Register your models here.
from.models import Shoppingcart
class ShoppingcartAdmin(admin.ModelAdmin):
    list_display=("product_id","product_name","product_price","product_quantity","product_image","vendor_id","date_added")
admin.site.register(Shoppingcart,ShoppingcartAdmin)

