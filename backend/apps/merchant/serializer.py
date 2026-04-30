from rest_framework import serializers
from .models import Merchant


class MarchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = "__all__"
