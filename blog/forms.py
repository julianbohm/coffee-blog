from django import forms
from .models import CoffeePost, Comment, Rating

class CoffeePostForm(forms.ModelForm):
    class Meta:
        model = CoffeePost
        fields = ['title', 'description', 'featured_image']
        exclude = ['slug', 'average_rating']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'rating']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stars']
        widgets = {
            'stars': forms.Select(attrs={
                'class': 'form-select',
                'id': 'id_stars',
                'required': True
            })
        }