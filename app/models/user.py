class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.events = {}

    def __repr__(self):
        return 'I am {}'.format(self.username)
