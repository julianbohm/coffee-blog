from django.contrib import admin
from .models import CoffeePost, Comment, Rating
from django_summernote.admin import SummernoteModelAdmin

# Custom admin panel for CoffeePost model
@admin.register(CoffeePost)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'date_posted')
    search_fields = ['title', 'description']
    list_filter = ('date_posted',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(Comment)
admin.site.register(Rating)