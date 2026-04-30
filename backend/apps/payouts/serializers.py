from rest_framework import serializers
from .models import Pay


class PaySerializer(serializers.ModelSerializer):
    merchant_name = serializers.CharField(source="merchant.name", read_only=True)

    class Meta:
        model = Pay
        fields = ["id", "amount", "status", "bank_ac_id", "time_st"]
