import unittest
from user import *

class TestUserFunctions(unittest.TestCase):

    def setUp(self):
        users_db.clear()
        users_db[1] = User(1, "Alice", 30) 
        users_db[2] = User(2, "Bob", 25)

    def test_get_user(self):
        user_data, status_code = get_user(1)
        # self.assertEqual(status_code, 200)
        self.assertEqual(user_data["name"], "Alice")
        self.assertEqual(user_data["age"], 30)

    def test_create_user(self):
        user_data, status_code = create_user("Charlie", 40)
        # self.assertEqual(status_code, 201)
        self.assertEqual(user_data["name"], "Charlie")
        self.assertEqual(user_data["age"], 40)

if __name__ == '__main__':
    unittest.main()