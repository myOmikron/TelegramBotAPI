class LoginUrl:
    def __init__(self, *, url, forward_text=None, bot_username=None, request_write_access=None):
        self.url = url
        self.forward_text = forward_text
        self.bot_username = bot_username
        self.request_write_access = request_write_access
