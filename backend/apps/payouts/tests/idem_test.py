import pytest
from django.test import Client
from apps.payouts.models import Pay


@pytest.mark.django_db
def test_idempotency():
    client = Client()

    key = "test_key"

    payload = {"amount": 100, "bank_ac_id": "bank1"}

    r1 = client.post(
        "/api/v1/payouts/",
        payload,
        content_type="application/json",
        HTTP_IDEMPOTENCY_KEY=key,
    )

    r2 = client.post(
        "/api/v1/payouts/",
        payload,
        content_type="application/json",
        HTTP_IDEMPOTENCY_KEY=key,
    )

    assert r1.json() == r2.json()

    assert r1.json()["id"] == r2.json()["id"]

    assert Pay.objects.count() == 1
