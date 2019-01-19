from django.db import models
from component.models import Component

TYPE_OF_MEAL = (
    ('SOUP', 'SOUP'),
    ('PIZZA', 'PIZZA'),
    ('FISH', 'FISH'),
    ('BURGER', 'BURGER'),
    ('OTHER', 'OTHER'),
)


class Meal(models.Model):
    components = models.ManyToManyField(Component)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    meal_type = models.CharField(max_length=8, choices=TYPE_OF_MEAL)
    quantity = models.IntegerField()
    description = models.FileField(null=True, blank=True)

    def decrease_meal_quantity(self):
        self.quantity -= 1

    def increase_meal_quantity(self):
        self.quantity += 1

    def __str__(self):
        return self.name
