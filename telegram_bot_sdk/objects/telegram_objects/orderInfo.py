from telegram_bot_sdk.objects.telegram_objects.shippingAddress import ShippingAddress


class OrderInfo:
    def __init__(self, *, name=None, phone_number=None, email=None, shipping_address=None):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.shipping_address = ShippingAddress(**shipping_address) if shipping_address else None
