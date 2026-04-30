from django.urls import path
from .view import MerchantView

urlpatterns = [
    path("balance/", MerchantView.as_view()),
]
