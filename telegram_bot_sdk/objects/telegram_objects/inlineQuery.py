from telegram_bot_sdk.objects.telegram_objects.location import Location
from telegram_bot_sdk.objects.telegram_objects.user import User


class InlineQuery:
    def __init__(self, *, id_unique=None, from_user=None, location=None, query=None, offset=None):
        self.id_unique = id_unique
        self.from_user = User(**from_user) if from_user else None
        self.location = Location(**location) if location else None
        self.query = query
        self.offset = offset
