from telegram_bot_sdk.objects.telegram_objects.inputMessageContent import InputMessageContent


class InputLocationMessageContent:
    def __init__(self, *, latitude, longitude, live_period):
        self.latitude = latitude
        self.longitude = longitude
        self.live_period = live_period
