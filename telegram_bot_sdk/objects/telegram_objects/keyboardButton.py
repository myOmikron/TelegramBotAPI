class KeyboardButton:
    def __init__(self, *, text, request_contact=None, request_location=None):
        self.text = text
        self.request_contact = request_contact
        self.request_location = request_location
