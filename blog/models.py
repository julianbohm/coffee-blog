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

    
    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

class Rating(models.Model):
    post = models.ForeignKey(CoffeePost, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f'{self.user} - {self.post} - {self.stars}'

class Comment(models.Model):
    post = models.ForeignKey(CoffeePost, on_delete=models.CASCADE, related_name='comments')  # Links to a blog post
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to a user
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date_posted"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"