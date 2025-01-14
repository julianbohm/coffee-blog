from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models import Avg
from cloudinary.models import CloudinaryField

# Create your models here.

class CoffeePost(models.Model):
    """
    stores a single blog post related to :model:auth.user".
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, editable=False)
    description = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder') 
    date_posted = models.DateTimeField(auto_now_add=True)
    average_rating = models.FloatField(default=0.0)

    
    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Rating(models.Model):
    post = models.ForeignKey(CoffeePost, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    class Meta:
        unique_together = ['post', 'user']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update average rating for the related CoffeePost
        self.post.average_rating = self.post.ratings.aggregate(Avg('stars'))['stars__avg'] or 0.0
        self.post.save()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        # Recalculate average rating after deleting
        self.post.average_rating = self.post.ratings.aggregate(Avg('stars'))['stars__avg'] or 0.0
        self.post.save()

    def __str__(self):
        return f'{self.user} - {self.post} - {self.stars}'

class Comment(models.Model):
    post = models.ForeignKey('CoffeePost', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(
        choices=[
            (1, "1 - Poor"),
            (2, "2 - Fair"),
            (3, "3 - Good"),
            (4, "4 - Very Good"),
            (5, "5 - Excellent")
        ],
        null=True,
        blank=True,  # Allow comments without ratings
    )
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date_posted"]

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"