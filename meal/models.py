from django.db import models
from component.models import Component


class Meal(models.Model):
    components = models.ManyToManyField(Component)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5,   decimal_places=2)
    TYPE_OF_MEAL = (
        ('SOUP', 'SOUP'),
        ('PIZZA', 'PIZZA'),
        ('FISH', 'FISH'),
        ('BURGER', 'BURGER'),
        ('OTHER', 'OTHER'),
    )
    meal_type = models.CharField(max_length=8, choices=TYPE_OF_MEAL)

    def __str__(self):
        return self.name


