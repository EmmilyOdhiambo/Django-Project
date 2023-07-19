from django.contrib import admin
from .models import Odermanage

class OdermanageAdmin(admin.ModelAdmin):
    list_display = ("name","price","total")


    def add_five_instances(self, request, queryset):
        for _ in range(5):
            Odermanage.objects.create(
                name='Tomatoes',
                price=10.99,
                total=54.95
            )
    
    add_five_instances.short_description = "Add Five Instances"  
    
    actions = [add_five_instances]  

admin.site.register(Odermanage,OdermanageAdmin)
