from telegram_bot_sdk.objects.telegram_objects.inputMessageContent import InputMessageContent


class InputTextMessageContent(InputMessageContent):
    def __init__(self, *, message_text, parse_mode=None, disable_web_page_preview=None):
        super().__init__()
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.disable_web_page_preview = disable_web_page_preview
