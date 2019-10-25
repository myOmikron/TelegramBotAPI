class ReplyKeyboardMarkup:
    def __init__(self, *, keyboard, resize_keyboard=None, one_time_keyboard=None, selective=None):
        self.keyboard = [ReplyKeyboardMarkup(**x) for x in keyboard]
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective
