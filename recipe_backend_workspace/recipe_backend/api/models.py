from django.db import models
from django.contrib.auth.models import User


# PUBLIC_INTERFACE
class Recipe(models.Model):
    """Model representing a recipe."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField(help_text="List of ingredients, separated by newline.")
    instructions = models.TextField(help_text="Preparation steps, separated by newline.")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
