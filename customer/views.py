from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer
from order.models import Order

from customer.forms import UserForm, CustomerForm


def index(request):
    return HttpResponse("Hello, world. You're at the customer index.")


@login_required
@transaction.atomic
def update_customer(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        customer_form = CustomerForm(request.POST, instance=request.user.customer)
        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            messages.success(request, 'Your profile was successfully updated')
            return redirect('settings:profile')
        else:
            messages.error(request, 'Please correct the error below')
    else:
        user_form = UserForm(request.POST, instance=request.user)
        customer_form = CustomerForm(request.POST, instance=request.user.customer)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'customer_form': customer_form
    })


def my_profile(request):
    my_customer_profile = Customer.objects.filter(user=request.user).first()
    my_orders = Order.objects.all()
    context = {
        'my_orders': my_orders
    }

    return render(request, "profile.html", context)


#def get_all_orders(request):
    #customers = Order.objects.all()
    #if request.method == 'POST':
     #   order = Order.objects.get(id=int(request.POST.get('orderId', False)))
     #   order.delete(order)

    #ctx = {
     #   'customer_order': customers
    #}
    #return render(request, "orders.html", ctx)
