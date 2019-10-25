from telegram_bot_sdk.objects.telegram_objects.location import Location
from telegram_bot_sdk.objects.telegram_objects.user import User


class ChosenInlineResult:
    def __init__(self, *, result_id=None, from_user=None, location=None, inline_message_id=None, query=None):
        self.result_id = result_id
        self.from_user = User(**from_user) if from_user else None
        self.location = Location(**location) if location else None
        self.inline_message_id = inline_message_id
        self.query = query
