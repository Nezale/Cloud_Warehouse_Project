from django.db import models
from address.models import Address
from django.contrib.auth.models import User


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
    password = User.password

