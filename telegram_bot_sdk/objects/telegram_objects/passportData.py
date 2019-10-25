from telegram_bot_sdk.objects.telegram_objects.encryptedCredentials import EncryptedCredentials
from telegram_bot_sdk.objects.telegram_objects.encryptedPassportElement import EncryptedPassportElement


class PassportData:
    def __init__(self, *, data, credentials):
        self.data = [EncryptedPassportElement(**x) for x in data] if data else None
        self.credentials = EncryptedCredentials(**credentials) if credentials else None
