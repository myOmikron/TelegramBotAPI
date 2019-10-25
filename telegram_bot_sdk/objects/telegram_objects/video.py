from telegram_bot_sdk.objects.telegram_objects.photoSize import PhotoSize


class Video:
    def __init__(self, *, file_id, width, height, duration, thumb=None, mime_type=None,
                 file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = PhotoSize(**thumb) if thumb else None
        self.mime_type = mime_type
        self.file_size = file_size
