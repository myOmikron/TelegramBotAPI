from telegram_bot_sdk.objects.telegram_objects.user import User


class MessageEntity:
    def __init__(self, *, type_result, offset, length, url=None, user=None):
        self.type_result = type_result
        self.offset = offset
        self.length = length
        self.url = url
        self.user = User(**user) if user else None
