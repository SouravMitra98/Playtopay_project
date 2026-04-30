from django.db import transaction
from rest_framework.exceptions import ValidationError

from apps.idempotency.models import IdemKey
from apps.payouts.services import payment_create
from apps.payouts.models import Pay


def idem_handler(request, merchant):
    key = request.headers.get("Idempotency-Key") or request.headers.get(
        "idempotency-key"
    )

    if not key:
        raise ValidationError("Idempotency-Key required")

    with transaction.atomic():
        idem, created = IdemKey.objects.get_or_create(
            merchant=merchant,
            key=key,
            defaults={"res": {}},
        )

        if not created:
            return idem.res

        amount = request.data.get("amount")
        bank = request.data.get("bank_ac_id")

        if not amount or not bank:
            raise ValidationError("Invalid payload")

        pay = payment_create(merchant, amount, bank)

        res = {
            "id": pay.id,
            "status": pay.status,
        }

        idem.res = res
        idem.save()

        return res
