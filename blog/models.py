from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CoffeePost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    average_rating = models.FloatField(default=0.0)