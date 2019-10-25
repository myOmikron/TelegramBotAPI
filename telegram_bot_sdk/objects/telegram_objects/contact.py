class Contact:
    def __init__(self, *, phone_number, first_name, last_name=None, user_id=None, vcard=None):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard
