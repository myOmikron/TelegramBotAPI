from telegram_bot_sdk.objects.telegram_objects.message import Message
from telegram_bot_sdk.objects.telegram_objects.user import User


class CallbackQuery:
    def __init__(self, *, id_unique, from_user, message=None, inline_message_id=None, chat_instance=None, data=None,
                 game_short_name=None):
        self.id_unique = id_unique
        self.from_user = User(**from_user)
        self.message = Message(**message) if message else None
        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name
