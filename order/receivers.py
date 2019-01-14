from django.dispatch import receiver
from .signals import *

@receiver(orderOrdered)
def decreaseMealAndComponentQuantity(sender, instance, **kwargs):
    return 0