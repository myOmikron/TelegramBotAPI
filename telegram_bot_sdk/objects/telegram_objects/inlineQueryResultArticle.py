from telegram_bot_sdk.objects.telegram_objects.inlineKeyboardMarkup import InlineKeyboardMarkup
from telegram_bot_sdk.objects.telegram_objects.inlineQueryResult import InlineQueryResult
from telegram_bot_sdk.objects.telegram_objects.inputMessageContent import InputMessageContent


class InlineQueryResultArticle(InlineQueryResult):
    def __init__(self, *, type_result, id_unique, title, input_message_content, reply_markup=None, url=None,
                 hide_url=None, description=None, thumb_url=None, thumb_width=None, thumb_height=None):
        super().__init__()
        self.type_result = type_result
        self.id_unique = id_unique
        self.title = title
        self.input_message_content = InputMessageContent(**input_message_content) if input_message_content else None
        self.reply_markup = InlineKeyboardMarkup(**reply_markup) if reply_markup else None
        self.url = url
        self.hide_url = hide_url
        self.description = description
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
