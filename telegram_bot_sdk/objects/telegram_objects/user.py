class User:
    def __init__(self, *, id_unique, is_bot, first_name, last_name=None, username=None, language_code=None):
        self.id_unique = id_unique
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
