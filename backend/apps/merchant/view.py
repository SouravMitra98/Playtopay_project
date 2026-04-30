from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from apps.merchant.models import Merchant
from apps.ledger.models import LegEntry
from common.const import CREDIT, DEBIT


class MerchantView(APIView):
    def get(self, request):
        merchant = Merchant.objects.first()

        if not merchant:
            return Response({"balance": 0, "held": 0})

        credits = (
            LegEntry.objects.filter(merchant=merchant, type=CREDIT).aggregate(
                Sum("amount")
            )["amount__sum"]
            or 0
        )

        debits = (
            LegEntry.objects.filter(merchant=merchant, type=DEBIT).aggregate(
                Sum("amount")
            )["amount__sum"]
            or 0
        )

        held = (
            LegEntry.objects.filter(
                merchant=merchant, type=DEBIT, pay__status="pending"
            ).aggregate(Sum("amount"))["amount__sum"]
            or 0
        )

        return Response(
            {
                "balance": credits - debits,
                "held": held,
                "available": (credits - debits) - held,
            }
        )
