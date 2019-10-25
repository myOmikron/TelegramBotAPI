class ShippingAddress:
    def __init__(self, *, country_code=None, state=None, city=None, street_line1=None,
                 street_line2=None, post_code=None):
        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code
