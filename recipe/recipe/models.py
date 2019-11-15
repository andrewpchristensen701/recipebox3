from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    """One to one relationship authentication"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    """One to many relationship authentication
    user = models.ForeignKey(User, on_delete=models.CASCADE)"""
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='TITLE OF RECIPE')
    description = models.TextField(default='RECIPE DESCRIPTION')
    time = models.IntegerField(default=1)
    instructions = models.TextField(default='RECIPE INSTRUCTIONS')
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.author.name}"