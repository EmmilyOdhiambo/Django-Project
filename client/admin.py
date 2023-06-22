from django.contrib import admin

# Register your models here.
from.models import Client
class ClientAdmin(admin.ModelAdmin):
    list_display=("username","email","password","first_name","last_name","phone_number","date_of_birth")
admin.site.register(Client,ClientAdmin)


