from django.db import models
from apps.merchant.models import Merchant


class IdemKey(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    res = models.JSONField()

    class Meta:
        unique_together = ("merchant", "key")
