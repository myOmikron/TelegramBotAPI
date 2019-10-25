from telegram_bot_sdk.objects.telegram_objects.photoSize import PhotoSize


class Animation:
    def __init__(self, *, file_id, width, height, duration, thumb=None, file_name=None, mime_type=None, file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = PhotoSize(**thumb) if thumb else None
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
