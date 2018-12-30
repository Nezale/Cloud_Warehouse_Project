from django.db import models
from shiping_method.models import ShippingMethod
from payment.models import Payment
from meal.models import Meal
from component.models import Component
from customer.models import Customer


class Order(models.Model):
    order_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Customer, on_delete= models.SET_NULL, null=True)
    meals = models.ManyToManyField(Meal, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField
    unit_price = models.DecimalField(max_digits=5,   decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    shipping_method = models.ForeignKey(ShippingMethod, null=True, on_delete=models.SET_NULL)
    payment = models.OneToOneField(Payment, on_delete=models.PROTECT)

    def get_cart_products(self):
        return self.meals.all()

    def get_cart_total(self):
        return sum([meal.price for meal in self.meals.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.order_date)
