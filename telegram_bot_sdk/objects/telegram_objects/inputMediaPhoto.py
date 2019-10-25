from telegram_bot_sdk.objects.telegram_objects import inputMedia


class InputMediaPhoto(inputMedia):
    def __init__(self, *, type_result, media, caption=None, parse_mode=None):
        self.type_result = type_result
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
