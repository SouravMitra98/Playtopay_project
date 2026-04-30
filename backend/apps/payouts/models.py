from django.db import models
from apps.merchant.models import Merchant


class Pay(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )
    bank_ac_id = models.CharField(max_length=255)
    time_st = models.DateTimeField(auto_now_add=True)

    def can_transition(self, new_status):
        transitions = {
            "pending": ["processing"],
            "processing": ["completed", "failed"],
            "completed": [],
            "failed": [],
        }

        current = (self.status or "").lower()

        return new_status in transitions.get(current, [])
