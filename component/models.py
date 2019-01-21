from django.db import models
from django.core.validators import MinValueValidator

class Component(models.Model):
    name = models.CharField(max_length=50)
    amount = models.SmallIntegerField(validators=[MinValueValidator(1)])
    price_per_dish = models.SmallIntegerField(validators=[MinValueValidator(1)])
    TYPE_OF_COMPONENT = (
        ('MEAT', 'MEAT'),
        ('CHEESE', 'CHEESE'),
        ('VEGETABLE', 'VEGETABLE'),
        ('FRUIT', 'FRUIT'),
        ('OTHER', 'OTHER'),
    )
    component_type = models.CharField(max_length=10, choices=TYPE_OF_COMPONENT)

    def decrease_component_amount(self):
        self.amount -= 1

    def increase_component_amount(self):
        self.amount += 1
        
    def __str__(self):
        return self.name
