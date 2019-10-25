from telegram_bot_sdk.objects.telegram_objects.chatPermissions import ChatPermissions
from telegram_bot_sdk.objects.telegram_objects.chatPhoto import ChatPhoto


class Chat:
    def __init__(self, *, id_unique, type_result, title=None, username=None, first_name=None, last_name=None,
                 photo=None, description=None, invite_link=None, pinned_message=None, permissions=None,
                 sticker_set_name=None, can_set_sticker_set=None):
        self.id_unique = id_unique
        self.type_result = type_result
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.photo = ChatPhoto(**photo) if photo else None
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.permissions = ChatPermissions(**permissions) if permissions else None
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set
