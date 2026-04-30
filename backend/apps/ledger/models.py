from django.db import models
from apps.merchant.models import Merchant
from apps.payouts.models import Pay


class LegEntry(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    type = models.CharField(max_length=10)  # credit or debit
    pay = models.ForeignKey(
        "payouts.Pay", on_delete=models.CASCADE, null=True, blank=True
    )
    tStamp = models.DateTimeField(auto_now_add=True)
