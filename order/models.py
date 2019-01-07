from django.db import models
from shiping_method.models import ShippingMethod
from payment.models import Payment
from meal.models import Meal
from component.models import Component
from customer.models import Customer


class OrderMeal(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.meal.name


class Order(models.Model):
    order_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    meals = models.ManyToManyField(OrderMeal, null=True, blank=True)
    ref_code = models.CharField(max_length=15, null=True)
    is_ordered = models.BooleanField(default=False)
    shipping_method = models.ForeignKey(ShippingMethod, null=True, on_delete=models.SET_NULL)
    payment = models.OneToOneField(Payment, on_delete=models.PROTECT, null=True)

    def get_cart_products(self):
        return self.meals.all()

    def get_cart_total(self):
        return sum([ meal.price for meal in self.meals.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.order_date)


class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    token = models.CharField(max_length=120)
    order_id= models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    success = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.order_id

    class Meta:
        ordering = ['-timestamp']
