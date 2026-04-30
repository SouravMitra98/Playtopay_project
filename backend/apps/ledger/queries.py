from django.db.models import Sum, Case, When, F, IntegerField
from .models import LegEntry


def get_bal(merchant):
    return (
        LegEntry.objects.filter(merchant=merchant).aggregate(
            balance=Sum(
                Case(
                    When(type="credit", then=F("amount")),
                    When(type="debit", then=-F("amount")),
                    output_field=IntegerField(),
                )
            )
        )["balance"]
        or 0
    )
