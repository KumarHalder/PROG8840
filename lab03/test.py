import unittest
from unittest.mock import MagicMock, patch
from user import Database

class TestDatabase(unittest.TestCase):
    @patch('sqlite3.connect')
    def setUp(self, mock_connect):
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        mock_connect.return_value = self.mock_conn
        self.mock_conn.cursor.return_value = self.mock_cursor
        self.db = Database('test.db')

    def test_insert_user(self):
        self.mock_cursor.lastrowid = 1
        user_id = self.db.insert_user('Alice', 30)
        self.assertEqual(user_id, 1)

    def test_get_user(self):
        self.mock_cursor.fetchone.return_value = (1, 'Alice', 30)
        user = self.db.get_user(1)
        self.assertEqual(user, (1, 'Alice', 30))

    def test_update_user(self):
        self.mock_cursor.rowcount = 1
        rows_affected = self.db.update_user(1, 'Bob', 35)
        self.assertEqual(rows_affected, 1)

    def test_delete_user(self):
        self.mock_cursor.rowcount = 1
        rows_affected = self.db.delete_user(1)
        self.assertEqual(rows_affected, 1)

    
if __name__ == '__main__':
    unittest.main()
