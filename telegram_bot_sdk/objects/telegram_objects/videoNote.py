from telegram_bot_sdk.objects.telegram_objects.photoSize import PhotoSize


class VideoNote:
    def __init__(self, *, file_id, length, duration, thumb=None, file_size=None):
        self.file_id = file_id
        self.length = length
        self.duration = duration
        self.thumb = PhotoSize(**thumb) if thumb else None
        self.file_size = file_size
