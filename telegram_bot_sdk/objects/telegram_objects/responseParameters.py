class ResponseParameters:
    def __init__(self, *, migrate_to_chat_id=None, retry_after=None):
        self.migrate_to_chat_id = migrate_to_chat_id
        self.retry_after = retry_after
