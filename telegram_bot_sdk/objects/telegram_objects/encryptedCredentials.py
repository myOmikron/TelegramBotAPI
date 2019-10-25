class EncryptedCredentials:
    def __init__(self, *, data, hash_data, secret):
        self.data = data
        self.hash_data = hash_data
        self.secret = secret
