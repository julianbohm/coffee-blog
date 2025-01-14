from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    # Additional field for rating
class RatingForm(forms.Form):
    rating = forms.ChoiceField(
        label="Rating",
        choices=[
            ("", "Select a rating"),
            ("1", "1 - Poor"),
            ("2", "2 - Fair"),
            ("3", "3 - Good"),
            ("4", "4 - Very Good"),
            ("5", "5 - Excellent"),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_rating',
            'required': True
        })
    )
