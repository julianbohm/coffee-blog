from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models import Avg
from cloudinary.models import CloudinaryField

# Create your models here.

class CoffeePost(models.Model):
    """
    Stores a single blog post related to :model:auth.user".
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    date_posted = models.DateTimeField(auto_now_add=True)
    post_rating = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0.0)

    class Meta:
        ordering = ["-date_posted"] # Newest posts first

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    def save(self, *args, **kwargs):
        """
        Overriding save method to automatically generate slug if not provided.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def update_average_rating(self):
        """
        Recalculate average rating based on user ratings and comment ratings.
        (Excludes the author's own 'post_rating')
        """
        all_ratings = (
            list(self.ratings.values_list('stars', flat=True)) +
            list(self.comments.exclude(rating__isnull=True).values_list('rating', flat=True))
        )
        if not all_ratings:
            self.average_rating = 0
        else:
            self.average_rating = round(sum(all_ratings) / len(all_ratings), 2)
        self.save()

class Rating(models.Model):
    """
    Model that stores a user's rating for a CoffeePost.
    """
    post = models.ForeignKey(CoffeePost, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    class Meta:
        unique_together = ['post', 'user'] # One rating per user per post

    def save(self, *args, **kwargs):
        """
        Update the post's average rating whenever a new rating is saved.
        """
        super().save(*args, **kwargs)
        self.post.update_average_rating()

    def delete(self, *args, **kwargs):
        """
        Update the post's average rating whenever a rating is deleted.
        """
        super().delete(*args, **kwargs)
        self.post.update_average_rating()

    def __str__(self):
        return f'{self.user} - {self.post} - {self.stars}'

class Comment(models.Model):
    """
    Model that stores a user's comment and optional rating on a CoffeePost.
    """
    post = models.ForeignKey(CoffeePost, on_delete=models.CASCADE, related_name='comments')
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
        ordering = ["date_posted"]  # Oldest comments first

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.post.update_average_rating()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.post.update_average_rating()

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
