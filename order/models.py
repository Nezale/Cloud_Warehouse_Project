from django.db import models
from shiping_method.models import ShippingMethod
from payment.models import Payment
from meal.models import Meal
from component.models import Component
from customer.models import Customer
from .signals import orderOrdered
from django.db.models.signals import post_save


class OrderMeal(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def increase_component_and_order_quantity(self):
        component_list = self.meal.components.all()
        self.meal.increase_meal_quantity()
        self.meal.save()
        for Component in component_list:
            Component.increase_component_amount()
            Component.save()
            
    def decrease_component_and_order_quantity(self):
        component_list = self.meal.components.all()
        self.meal.decrease_meal_quantity()
        self.meal.save()
        for Component in component_list:
            Component.decrease_component_amount()
            Component.save()

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
        return sum([meal.meal.price for meal in self.meals.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.order_date)


class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    token = models.CharField(max_length=120)
    order_id = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    success = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.order_id

    class Meta:
        ordering = ['-timestamp']
