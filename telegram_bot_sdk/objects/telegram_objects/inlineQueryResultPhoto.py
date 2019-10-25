from telegram_bot_sdk.objects.telegram_objects.inlineKeyboardMarkup import InlineKeyboardMarkup
from telegram_bot_sdk.objects.telegram_objects.inlineQueryResult import InlineQueryResult
from telegram_bot_sdk.objects.telegram_objects.inputMessageContent import InputMessageContent


class InlineQueryResultPhoto(InlineQueryResult):
    def __init__(self, *, type_result, id_unique, photo_url, thumb_url, photo_width=None, photo_height=None, title=None,
                 description=None, caption=None, parse_mode=None, reply_markup=None, input_message_content=None):
        super().__init__()
        self.type_result = type_result
        self.id_unique = id_unique
        self.photo_url = photo_url
        self.thumb_url = thumb_url
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.reply_markup = InlineKeyboardMarkup(**reply_markup) if reply_markup else None
        self.input_message_content = InputMessageContent(**input_message_content) if input_message_content else None
