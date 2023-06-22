from django.contrib import admin

# Register your models here.
from.models import Ratings
class RatingsAdmin(admin.ModelAdmin):
    list_display=("id","title","review_content","rating","cumulative_ratings","created_date")
admin.site.register(Ratings,RatingsAdmin)

