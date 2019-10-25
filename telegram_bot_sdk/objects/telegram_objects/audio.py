from telegram_bot_sdk.objects.telegram_objects.photoSize import PhotoSize


class Audio:
    def __init__(self, *, file_id, duration, performer=None, title=None, mime_type=None, file_size=None, thumb=None):
        self.file_id = file_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumb = PhotoSize(**thumb) if thumb else None
