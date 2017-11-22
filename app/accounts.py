class Accounts:
    def __init__(self):
        # We need to store every user of the system
        self.users = {}

    def add_user(self, user):
        # Adds a user to current users
        self.users.update({user.email: user})
        # self.users[user.email] = user

    def remove_user(self, user):
        self.users.pop(user.email)
