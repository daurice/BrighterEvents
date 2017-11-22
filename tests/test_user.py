import unittest

from app.accounts import Accounts
from app.models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('Doris', 'doris@gmail.com', 'forwhatfor')
        self.accounts = Accounts()
        self.accounts.add_user(self.user)

    def test_add_user(self):
        # Tests if a user Is Successfully created
        self.assertEqual(1, len(self.accounts.users))

    def test_remove_user(self):
        self.assertEqual(1, len(self.accounts.users))
        self.accounts.remove_user(self.user)
        self.assertEqual(0, len(self.accounts.users))


if __name__ == '__main__':
    unittest.run()
