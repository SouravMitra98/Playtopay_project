from django.urls import path, include

urlpatterns = [
    path("api/v1/payouts/", include("apps.payouts.urls")),
    path("api/v1/", include("apps.merchant.urls")),
]
