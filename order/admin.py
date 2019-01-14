from django.contrib import admin
from .models import OrderMeal, Order, Transaction

admin.site.register(OrderMeal)
admin.site.register(Order)
admin.site.register(Transaction)
