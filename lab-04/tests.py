"""Tests for the main.py file."""
import unittest
from main import app


class TestHelloWorldRoute(unittest.TestCase):
    """Test that the root route returns a simple "Hello, World!" message.
    """

    def setUp(self):
        self.app = app.test_client()

    def test_hello_world_route(self):
        """Test that the root route returns a simple "Hello, World!" message"""

        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'<p>Hello, World!</p>')

    def test_delete_route(self):
        """Test that the delete route returns a simple "Delete" message."""

        response = self.app.get('/delete')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'<p>Delete</p>')


if __name__ == '__main__':
    unittest.main()
