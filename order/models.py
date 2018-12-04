from django.db import models
from shiping_method.models import ShippingMethod
from payment.models import Payment


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField
    unit_price = models.DecimalField(max_digits=5,   decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    shipping_method = models.ForeignKey(ShippingMethod, on_delete=models.SET_NULL)
    payment = models.OneToOneField(Payment, on_delete=models.PROTECT)
