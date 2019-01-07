from django.conf import settings
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from meal.models import Meal
from order.models import Order, Transaction, OrderMeal
from order.extras import generate_order_id, transact, generate_client_token
from customer.models import Customer

import datetime
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_customer_pending_order(request):
    customer = get_object_or_404(Customer, user=request.user)
    order = Order.objects.filter(owner=customer, is_ordered=False)
    if order.exists():
        return order[0]
    return 0


@login_required
def add_to_cart(request, **kwargs):
    customer = get_object_or_404(Customer, user=request.user)
    meal = Meal.objects.filter(id=kwargs.get('item_id', "")).first()
    order_meal = OrderMeal.objects.create(meal=meal)
    order_meal.save()
    customer_order, status = Order.objects.get_or_create(owner=customer, is_ordered=False)
    customer_order.meals.add(order_meal)
    if status:
        customer_order.ref_code = generate_order_id()
        customer_order.save()

    customer.orders.add(customer_order)
    messages.info(request, "Meal added to cart")
    return redirect(reverse('meal:meals-list'))


@login_required
def delete_from_cart(request, item_id):
    meal_to_delete = OrderMeal.objects.filter(pk=item_id)
    if meal_to_delete.exists():
        meal_to_delete[0].delete()
        messages.info(request,"Meal has been deleted from cart")

    return redirect(reverse('order:order_summary'))


@login_required
def order_details(request, **kwargs):
    existing_order = get_customer_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'order_summary.html',context)


def checkout(request, **kwargs):
    customer_token = generate_client_token()
    existing_order = get_customer_pending_order(request)
    publish_key = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        token = request.POST.get('stripeToken', False)
        if token:
            try:
                charge = stripe.Charge.create(
                    amount=100*existing_order.get_cart_total(),
                    currency='pln',
                    descriptions='cloud_meals_warehouse',
                    source=token,
                )

                return redirect(reverse('order:update_records',
                        kwargs={
                            'token': token
                        })
                        )
            except stripe.CardError as e:
                messages.info(request, "Your card has been declined")

        else:
            result = transact({
                'amount': existing_order.get_cart_total(),
                'payment_method_nonce': request.POST['payment_method_nonce'],
                'options': {
                    "submit_for_settlement": True
                }
            })

            if result.is_success or result.transaction:
                return redirect(reverse('order:update_records',
                                        kwargs={
                                            'token': result.transaction.id
                                        })
                                )
            else:
                for x in result.errors.deep_errors:
                    messages.info(request, x)

                return redirect(reverse('order:checkout'))

    context = {
        'order': existing_order,
        'client_token': customer_token,
        'STRIPE_PUBLISHABLE_KEY': publish_key
    }

    return render(request, 'order/checkout.html', context)


@login_required
def update_transaction_records(request, token):
    order_to_purchase = get_customer_pending_order(request)

    order_to_purchase.is_ordered = True
    order_to_purchase.order_date = datetime.datetime.now()
    order_to_purchase.save()

    order_meals = order_to_purchase.meals.all()

    order_meals.update(date_ordered=datetime.datetime.now())

    customer_profile = get_object_or_404(Customer, user=request.user)


    # order_products = [item.meal for item in order_meals]
    # trzeba dodac jakos order w tym miejscu do customera jeszcze nie wiem jak, jak ktos wie to zrobcie to plx
    #customer_profile.orders.add(*)

    customer_profile.save()

    transaction = Transaction(customer=request.user.customer,
                              token= token,
                              order_id = order_to_purchase.id,
                              amount= order_to_purchase.get_cart_total(),
                              success= True)
    transaction.save()

    messages.info(request, "Thank you! Your purchase was successfull !")
    return redirect(reverse('customer:my_profile'))


@login_required
def success(request, **kwargs):
    return render(request, 'order/purchase_success.html', {})

