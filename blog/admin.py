from django.contrib import admin
from .models import CoffeePost, Comment

# Register your models here.

admin.site.register(CoffeePost)
admin.site.register(Comment)