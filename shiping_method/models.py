from django.db import models


class ShippingMethod(models.Model):
    method = models.CharField(max_length=30)

