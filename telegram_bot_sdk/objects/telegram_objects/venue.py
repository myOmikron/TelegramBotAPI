from telegram_bot_sdk.objects.telegram_objects.location import Location


class Venue:
    def __init__(self, *, location, title, address, foursquare_id=None, foursquare_type=None):
        self.location = Location(**location)
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
