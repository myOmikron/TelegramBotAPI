from telegram_bot_sdk.objects.telegram_objects.maskPosition import MaskPosition
from telegram_bot_sdk.objects.telegram_objects.photoSize import PhotoSize


class Sticker:
    def __init__(self, *, file_id=None, width=None, height=None, is_animated=None, thumb=None, emoji=None,
                 set_name=None, mask_position=None, file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.is_animated = is_animated
        self.thumb = PhotoSize(**thumb) if thumb else None
        self.emoji = emoji
        self.set_name = set_name
        self.mask_position = MaskPosition(**mask_position) if mask_position else None
        self.file_size = file_size
