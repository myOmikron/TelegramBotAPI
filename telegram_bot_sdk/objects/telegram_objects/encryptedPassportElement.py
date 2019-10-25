from telegram_bot_sdk.objects.telegram_objects.passportFile import PassportFile


class EncryptedPassportElement:
    def __init__(self, *, type_result, data, hash_data, phone_number=None, email=None, files=None, front_side=None,
                 reverse_side=None, selfie=None, translation=None):
        self.type_result = type_result
        self.data = data
        self.hash_data = hash_data
        self.phone_number = phone_number
        self.email = email
        self.files = [PassportFile(**x) for x in files] if files else None
        self.front_side = PassportFile(**front_side) if front_side else None
        self.reverse_side = PassportFile(**reverse_side) if reverse_side else None
        self.selfie = PassportFile(**selfie) if selfie else None
        self.translation = [PassportFile(**x) for x in translation] if translation else None
