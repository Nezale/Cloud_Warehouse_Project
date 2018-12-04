from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    state = models.CharField(max_length=30)
    street = models.CharField(max_length=30)


