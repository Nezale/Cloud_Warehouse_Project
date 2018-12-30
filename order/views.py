from django.shortcuts import render
from django.http import HttpResponse
from customer.models import Customer
from meal.models import Meal


def add_to_cart(request, **kwargs):
    user_customer = get_object_or_404(Customer, user=request.user)
    meals = Meal.objects.filter(id=kwargs.get('meal_id', "")).all()

