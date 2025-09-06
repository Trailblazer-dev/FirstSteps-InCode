from django.db import models

# Create your models here.
class Pizza(models.Model):
    """Pizza model."""
    name = models.CharField(max_length=200)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.name
    
class Topping(models.Model):
    """Pizza topping model. Each topping is associated with a specific pizza."""
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.name
    
    
