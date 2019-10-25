from telegram_bot_sdk.objects.telegram_objects.photoSize import PhotoSize


class UserProfilePhotos:
    def __init__(self, *, total_count, photos):
        self.total_count = total_count
        self.photos = [PhotoSize(**x) for x in photos] if photos else None
