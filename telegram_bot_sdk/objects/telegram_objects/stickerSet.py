from telegram_bot_sdk.objects.telegram_objects.sticker import Sticker


class StickerSet:
    def __init__(self, *, name, title, is_animated, contains_masks, stickers):
        self.name = name
        self.title = title
        self.is_animated = is_animated
        self.contains_masks = contains_masks
        self.stickers = [Sticker(**x) for x in stickers] if stickers else None
