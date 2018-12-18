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
    _price = models.DecimalField(max_digits=5,   decimal_places=2, db_column='price', blank=True, null=True)
    meal_type = models.CharField(max_length=8, choices=TYPE_OF_MEAL)

    def __str__(self):
        return self.name

    def save(self):
        super().save()

    @property
    def price(self):
        for i in range(0, len(self.components)):
            self._price += self.components[i].price
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
