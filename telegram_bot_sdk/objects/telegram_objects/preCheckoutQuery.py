from telegram_bot_sdk.objects.telegram_objects.orderInfo import OrderInfo
from telegram_bot_sdk.objects.telegram_objects.user import User


class PreCheckoutQuery:
    def __init__(self, *, id_unique=None, from_user=None, currency=None, total_amount=None, invoice_payload=None,
                 shipping_option_id=None, order_info=None):
        self.id_unique = id_unique
        self.from_user = User(**from_user) if from_user else None
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = OrderInfo(**order_info) if order_info else None
