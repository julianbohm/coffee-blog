from django.contrib import admin
from .models import CoffeePost, Comment, Rating

# Register your models here.

admin.site.register(CoffeePost)
admin.site.register(Comment)
admin.site.register(Rating)