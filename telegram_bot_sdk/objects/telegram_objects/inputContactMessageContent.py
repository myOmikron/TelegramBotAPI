from telegram_bot_sdk.objects.telegram_objects.inputMessageContent import InputMessageContent


class InputContactMessageContent:
    def __init__(self, *, phone_number, first_name, last_name=None, vcard=None):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard
