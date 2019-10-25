from telegram_bot_sdk.objects.telegram_objects.inlineKeyboardButton import InlineKeyboardButton


class InlineKeyboardMarkup:
    def __init__(self, *, inline_keyboard):
        for item in inline_keyboard:
            for entry in item:
                print(type(entry))
        self.inline_keyboard = inline_keyboard
