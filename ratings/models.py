from django.db import models

# Create your models here.

class Ratings(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    review_content = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    cumulative_ratings = models.IntegerField()
    
    created_date = models.DateTimeField(auto_now_add=True)
   
