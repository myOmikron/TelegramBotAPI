from telegram_bot_sdk.objects.telegram_objects.pollOption import PollOption


class Poll:
    def __init__(self, *, id_unique, question, options, is_closed):
        self.id_unique = id_unique
        self.question = question
        self.options = [PollOption(**x) for x in options] if options else None
        self.is_closed = is_closed
