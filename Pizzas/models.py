from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pizza_name
    
class Topping(models.Model):
    pizza= models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name=models.CharField(max_length=200)
    date_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topping_name
