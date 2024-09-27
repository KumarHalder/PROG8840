import unittest
from user import get_user, create_user, update_user, list_users

class TestUser(unittest.TestCase):
    def test_get_user_success(self):
        user, status_code = get_user(1)
        self.assertEqual(status_code, 200)
        self.assertEqual(user['name'], 'Alice')

    def test_get_user_not_found(self):
        user, status_code = get_user(10)
        self.assertEqual(status_code, 404)
        self.assertEqual(user['error'], 'User not found')

    def test_create_user_success(self):
        user, status_code = create_user('Charlie', 35)
        self.assertEqual(status_code, 201)
        self.assertEqual(user['name'], 'Charlie')

    def test_update_user_success(self):
        user, status_code = update_user(1, 'Alice', 31)
        self.assertEqual(status_code, 200)
        self.assertEqual(user['name'], 'Alice')

    def test_update_user_not_found(self):
        user, status_code = update_user(10, 'Charlie', 35)
        self.assertEqual(status_code, 404)
        self.assertEqual(user['error'], 'User not found')

    def test_list_users_success(self):
        users, status_code = list_users()
        self.assertEqual(status_code, 200)
        self.assertEqual(len(users), 3)

if __name__ == '__main__':
    unittest.main()


