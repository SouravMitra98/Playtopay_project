from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.merchant.models import Merchant
from apps.idempotency.services import idem_handler
from apps.payouts.models import Pay
from .serializers import PaySerializer


class PayView(APIView):

    def get(self, request):
        payouts = Pay.objects.all().order_by("-time_st")
        data = PaySerializer(payouts, many=True).data
        return Response(data)

    def post(self, request):
        merchant = Merchant.objects.first()

        if not merchant:
            return Response({"error": "No merchant"}, status=400)

        try:
            res = idem_handler(request, merchant)
            return Response(res)
        except Exception as e:
            print("ERROR:", str(e))
            return Response({"error": str(e)}, status=400)
