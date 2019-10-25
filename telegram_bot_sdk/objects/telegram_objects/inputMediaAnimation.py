from telegram_bot_sdk.objects.telegram_objects import inputMedia
from telegram_bot_sdk.objects.telegram_objects.inputFile import InputFile


class InputMediaAnimation(inputMedia):
    def __init__(self, *, type_result, media, thumb=None, caption=None, parse_mode=None, width=None,
                 height=None, duration=None):
        self.type_result = type_result
        self.media = media

        if type(thumb).__name__ is 'InputFile':
            self.thumb = InputFile(**thumb)
        else:
            self.thumb = thumb
        self.caption = caption
        self.parse_mode = parse_mode
        self.width = width
        self.height = height
        self.duration = duration
