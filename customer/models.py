from django.db import models
from address.models import Address
from django.contrib.auth.models import User
from order.models import Order


class Customer(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    address = models.OneToOneField(Address,
                                   on_delete=models.PROTECT,
                                   primary_key=True,
                                   )
    company_name = models.CharField(max_length=50)
    orders = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    password = User.password

    def __str__(self):
        return self.name + " " + self.surname
