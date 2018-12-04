from django.db import models
from payment_method.models import PaymentMethod


class Payment(models.Model):
    paymentMethod = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)
    paymentAmount = models.DecimalField(max_digits=5, decimal_places=2)
    paymentDate = models.DateTimeField(auto_now_add=True)
    creditCardMember = models.CharField(max_length=50)
    creditCardEXPCode = models.CharField(max_length=7)
    cardHoldersName = models.CharField(max_length=30)

