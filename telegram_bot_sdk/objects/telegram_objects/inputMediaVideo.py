from telegram_bot_sdk.objects.telegram_objects import inputMedia


class InputMediaVideo(inputMedia):
    def __init__(self, *, type_result, media, thumb=None, caption=None, parse_mode=None, width=None, height=None,
                 duration=None, supports_streaming=None):
        self.type_result = type_result
        self.media = media
        if type(thumb).__name__ is 'InputFile':
            self.thumb = thumb
        else:
            self.thumb = thumb
        self.caption = caption
        self.parse_mode = parse_mode
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming
