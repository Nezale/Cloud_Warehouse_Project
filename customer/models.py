from django.db import models
from address.models import Address
from django.contrib.auth.models import User
from order.models import Order
from django.db.models.signals import post_save
from django.dispatch import receiver


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, blank=True)
    address = models.OneToOneField(Address,
                                   on_delete=models.CASCADE,
                                   blank=True,
                                   null=True
                                   )
    company_name = models.CharField(max_length=50, blank=True)
    orders = models.ForeignKey(Order,
                               null=True,
                               on_delete=models.CASCADE,
                               blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


@receiver(post_save, sender=User)
def create_user_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_customer(sender, instance, **kwargs):
    instance.customer.save()


