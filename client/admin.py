from django.contrib import admin

# Register your models here.
from.models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display=("username","email","password","first_name","last_name","phone_number")
    # admin.site.register(Client,ClientAdmin)
admin.site.register(Client,ClientAdmin)