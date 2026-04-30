from django.db import transaction
from django.db.models import Sum, Case, When, F, IntegerField
from apps.ledger.models import LegEntry
from .models import Pay
from apps.payouts.tasks import process_pay
from django.db import transaction


@transaction.atomic
def payment_create(merchant, amount, bank):
    list(LegEntry.objects.select_for_update().filter(merchant=merchant))

    bal = (
        LegEntry.objects.filter(merchant=merchant).aggregate(
            total=Sum(
                Case(
                    When(type="credit", then=F("amount")),
                    When(type="debit", then=-1 * F("amount")),
                    output_field=IntegerField(),
                )
            )
        )["total"]
        or 0
    )

    if bal < amount:
        raise Exception("Insufficient Balance")

    payout = Pay.objects.create(merchant=merchant, amount=amount, bank_ac_id=bank)

    LegEntry.objects.create(merchant=merchant, amount=amount, type="debit", pay=payout)

    list(LegEntry.objects.select_for_update().filter(merchant=merchant))

    process_pay(payout.id)

    # transaction.on_commit(lambda: process_pay.delay(payout.id))
    return payout
