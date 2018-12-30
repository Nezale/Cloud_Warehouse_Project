from django.urls import path, re_path
from django.conf.urls import url

from .views import (
    add_to_cart,
    delete_from_cart,
    order_details,
    checkout,
    process_payment,
    update_transaction_records,
    success
)

from . import views

app_name = 'order'

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^add-to-cart/(?P<meal_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    url(r'^order-summary/$', order_details, name="order_summary"),
    url(r'^success/$', success, name="purchase_success"),
    url(r'^meal/delete/(?P<meal_id>[-w\]+)/$', delete_from_cart, name="delete_from_cart"),
    url(r'^checkout/$', checkout, name="checkout"),
    url(r'^payment/(?P<order_id>[-\w]+)/$', process_payment, name="process_payment"),
    url(r'^update-transaction/(?P<order_id>[-\w]+)/s', update_transaction_records, name="update_records")
]
