
import pytest
from main import app, books

@pytest.fixture
def client():
    """
    A pytest fixture to create a test client for the application.

    This fixture can be used to send requests to the application and
    test its responses. 
    
    Note: This test suit does not follow best practices of unit tests. This is for demo purposes. 

    Yields:
        flask.testing.FlaskClient: A test client for the application.
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_create_book(client):
    data = {"title": "New Book", "author": "New Author"}
    response = client.post("/books", json=data)
    assert response.status_code == 201
    assert len(books) == 3
    assert books[-1]["title"] == "New Book"
    assert books[-1]["author"] == "New Author"

def test_get_books(client):
    response = client.get("/books")
    assert response.status_code == 200
    assert len(response.json) == 3

def test_get_book(client):
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json["title"] == "Book 1"
    assert response.json["author"] == "Author 1"

def test_update_book(client):
    data = {"title": "Updated Book", "author": "Updated Author"}
    response = client.put("/books/1", json=data)
    assert response.status_code == 200
    assert books[0]["title"] == "Updated Book"
    assert books[0]["author"] == "Updated Author"

def test_delete_book(client):
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert len(books) == 2
