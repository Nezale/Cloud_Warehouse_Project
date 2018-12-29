from django.db import models


class PaymentMethod(models.Model):
    method = models.CharField(max_length=30)

    def __str__(self):
        return self.method
