from telegram_bot_sdk.objects.telegram_objects.animation import Animation
from telegram_bot_sdk.objects.telegram_objects.messageEntity import MessageEntity
from telegram_bot_sdk.objects.telegram_objects.photoSize import PhotoSize


class Game:
    def __init__(self, *, title=None, description=None, photo=None, text=None, text_entities=None, animation=None):
        self.title = title
        self.description = description
        self.photo = [PhotoSize(**x) for x in photo] if photo else None
        self.text = text
        self.text_entities = [MessageEntity(**x) for x in text_entities] if text_entities else None
        self.animation = Animation(**animation) if animation else None
