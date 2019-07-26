from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Ebook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title


class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    review_author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    ebook = models.ForeignKey(
        Ebook, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return str(self.rating)
