class PhotoSize:
    def __init__(self, *, file_id, width, height, file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.file_size = file_size
