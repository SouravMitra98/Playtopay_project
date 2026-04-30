from random import random
from django.db import transaction
from apps.ledger.models import LegEntry
from apps.payouts.models import Pay
from common.const import CREDIT


def process_pay(pay_id):
    
    with transaction.atomic():
        payout = Pay.objects.select_for_update().get(id=pay_id)

        if not payout.can_transition("processing"):
            return

        payout.status = "processing"
        payout.save()

    r = random()

    
    if r < 0.7:
        with transaction.atomic():
            payout = Pay.objects.select_for_update().get(id=pay_id)

            if not payout.can_transition("completed"):
                return

            payout.status = "completed"
            payout.save()
        return

    
    if r < 0.9:
        with transaction.atomic():
            payout = Pay.objects.select_for_update().get(id=pay_id)

            if not payout.can_transition("failed"):
                return

            already_refunded = LegEntry.objects.filter(
                pay=payout, type=CREDIT
            ).exists()

            if not already_refunded:
                LegEntry.objects.create(
                    merchant=payout.merchant,
                    amount=payout.amount,
                    type=CREDIT,
                    pay=payout,
                )

            payout.status = "failed"
            payout.save()
        return
    with transaction.atomic():
        payout = Pay.objects.select_for_update().get(id=pay_id)

        if payout.can_transition("failed"):
            payout.status = "failed"
            payout.save()
