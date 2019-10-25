class WebhookInfo:
    def __init__(self, *, url, has_custom_certificate=None, pending_update_count=None, last_error_date=None,
                 last_error_message=None, max_connections=None, allowed_updates=None):
        self.url = url
        self.has_custom_certificate = has_custom_certificate
        self.pending_update_count = pending_update_count
        self.last_error_date = last_error_date
        self.last_error_message = last_error_message
        self.max_connections = max_connections
        self.allowed_update = [x for x in allowed_updates] if allowed_updates else None
