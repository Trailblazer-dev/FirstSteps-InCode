from django.db import models

# Create your models here.

class MealPlan(models.Model):
    """Meal plan model to store meal plan details."""
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name