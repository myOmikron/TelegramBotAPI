from telegram_bot_sdk.objects.telegram_objects.shippingAddress import ShippingAddress
from telegram_bot_sdk.objects.telegram_objects.user import User


class ShippingQuery:
    def __init__(self, *, id_unique=None, from_user=None, invoice_payload=None, shipping_address=None):
        self.id_unique = id_unique
        self.from_user = User(**from_user) if from_user else None
        self.invoice_payload = invoice_payload
        self.shipping_address = ShippingAddress(**shipping_address) if shipping_address else None
