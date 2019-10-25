from telegram_bot_sdk.objects.telegram_objects.orderInfo import OrderInfo


class SuccessfulPayment:
    def __init__(self, currency, total_amount, invoice_payload, telegram_payment_charge_id,
                 provider_payment_charge_id=None, shipping_option_id=None, order_info=None):
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id
        self.shipping_option_id = shipping_option_id
        self.order_info = OrderInfo(**order_info) if order_info else None
