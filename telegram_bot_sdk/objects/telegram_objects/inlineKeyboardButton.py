from telegram_bot_sdk.objects.telegram_objects.callbackGame import CallbackGame
from telegram_bot_sdk.objects.telegram_objects.loginUrl import LoginUrl


class InlineKeyboardButton:
    def __init__(self, *, text, url=None, login_url=None, callback_data=None, switch_inline_query=None,
                 switch_inline_query_current_chat=None, callback_game=None, pay=None):
        self.text = text
        self.url = url
        self.login_url = LoginUrl(**login_url) if login_url else None
        self.callback_data = callback_data
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.callback_game = CallbackGame(**callback_game) if callback_game else None
        self.pay = pay
