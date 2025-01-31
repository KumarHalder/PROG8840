import unittest
from unittest.mock import patch
from user import User, get_user, create_user


### AAA - Arrange, Act and Assert
class TestUserFunctions(unittest.TestCase):
    @patch('user.users_db')
    def test_get_user(self, mock_users_db):
        # Arrange 
        mock_users_db.get.return_value = None
        
        # Act
        result = get_user(1)
        
        # Assert
        self.assertEqual(result, ({'error': 'User not found'}, 404))
        mock_users_db.get.assert_called_once_with(1)

        # AAA
        mock_users_db.get.return_value = User(1, 'Alice', 30)
        
        result = get_user(1)
        
        self.assertEqual(result, ({'user_id': 1, 'name': 'Alice', 'age': 30}, 200))
        mock_users_db.get.assert_called_with(1)

    @patch('user.users_db')
    def test_create_user(self, mock_users_db):
        mock_users_db.get.return_value = None
        
        result = create_user('Bob', 25)
        
        self.assertEqual(result, ({'user_id': 1, 'name': 'Bob', 'age': 25}, 201))


if __name__ == '__main__':
    unittest.main()