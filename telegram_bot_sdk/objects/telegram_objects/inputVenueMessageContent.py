class InputVenueMessageContent:
    def __init__(self, *, latitude, longitude, title, address, foursquare_id=None, foursquare_type=None):
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
