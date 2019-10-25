from telegram_bot_sdk.objects.telegram_objects.callbackQuery import CallbackQuery
from telegram_bot_sdk.objects.telegram_objects.message import Message
from telegram_bot_sdk.objects.telegram_objects.inlineQuery import InlineQuery
from telegram_bot_sdk.objects.telegram_objects.chosenInlineResult import ChosenInlineResult
from telegram_bot_sdk.objects.telegram_objects.poll import Poll
from telegram_bot_sdk.objects.telegram_objects.preCheckoutQuery import PreCheckoutQuery
from telegram_bot_sdk.objects.telegram_objects.shippingQuery import ShippingQuery


class Update:
    def __init__(self, *, update_id, message=None, edited_message=None, channel_post=None,
                 edited_channel_post=None, inline_query=None, chosen_inline_result=None, callback_inline_result=None,
                 shipping_query=None, pre_checkout_query=None, poll=None):
        self.update_id = update_id
        self.message = Message(**message) if message else None
        self.edited_message = Message(**edited_message) if edited_message else None
        self.channel_post = Message(**channel_post) if channel_post else None
        self.edited_channel_post = Message(**edited_channel_post) if edited_channel_post else None
        self.inline_query = InlineQuery(**inline_query) if inline_query else None
        self.chosen_inline_result = ChosenInlineResult(**chosen_inline_result) if chosen_inline_result else None
        self.callback_inline_result = CallbackQuery(**callback_inline_result) if callback_inline_result else None
        self.shipping_query = ShippingQuery(**shipping_query) if shipping_query else None
        self.pre_checkout_query = PreCheckoutQuery(**pre_checkout_query) if pre_checkout_query else None
        self.poll = Poll(**poll) if poll else None
