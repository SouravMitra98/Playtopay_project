from apps.merchant.models import Merchant
from apps.ledger.models import LegEntry
from common.const import CREDIT


def seed():
    merchants = ["merchant1", "merchant2", "merchant3"]

    for name in merchants:
        merchant, _ = Merchant.objects.get_or_create(name=name)

        # seed only if no ledger exists
        if not LegEntry.objects.filter(merchant=merchant).exists():
            LegEntry.objects.bulk_create(
                [
                    LegEntry(merchant=merchant, amount=50000, type=CREDIT),
                    LegEntry(merchant=merchant, amount=20000, type=CREDIT),
                    LegEntry(merchant=merchant, amount=30000, type=CREDIT),
                ]
            )

        print(f"Seeded: {merchant.name} (id={merchant.id})")
