from django.db import models


class Component(models.Model):
    name = models.CharField(max_length=50)
    amount = models.SmallIntegerField()
    price_per_dish = models.SmallIntegerField()
    TYPE_OF_COMPONENT = (
        ('MEAT', 'MEAT'),
        ('CHEESE', 'CHEESE'),
        ('VEGETABLE', 'VEGETABLE'),
        ('FRUIT', 'FRUIT'),
        ('OTHER', 'OTHER'),
    )
    component_type = models.CharField(max_length=10, choices=TYPE_OF_COMPONENT)

    def __str__(self):
        return self.name
