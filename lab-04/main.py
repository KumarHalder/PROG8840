from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store for books
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"}
]


@app.route("/books", methods=["POST"])
def create_book():
    """
    Create a new book resource.

    Args:
        title (str): The title of the book.
        author (str): The author of the book.

    Returns:
        dict: The newly created book resource.
    """
    # Create a new book with the next ID
    new_book = {
        "id": len(books) + 1,
        # Use the title from the request body
        "title": request.json["title"],
        # Use the author from the request body
        "author": request.json["author"]
    }
    # Add the new book to the list
    books.append(new_book)
    # Return the new book with a 201 status code
    return jsonify(new_book), 201


@app.route("/books", methods=["GET"])
def get_books():
    """
    Get the list of all books.

    Returns:
        list: The list of all books.
    """
    # Return the list of books
    return jsonify(books)


@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    """
    Get a single book by ID.

    Args:
        book_id (int): The ID of the book to retrieve.

    Returns:
        dict: The book with the given ID, or a 404 error if the book is not
            found.
    """
    # Find the book by ID
    book = next((book for book in books if book["id"] == book_id), None)
    # If the book is not found, return a 404 error
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    # Otherwise, return the book
    return jsonify(book)


@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    """
    Update a single book by ID.

    Args:
        book_id (int): The ID of the book to update.

    Returns:
        dict: The updated book with the given ID, or a 404 error if the book is
            not found.
    """
    # Find the book by ID
    book = next((book for book in books if book["id"] == book_id), None)
    # If the book is not found, return a 404 error
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    # Otherwise, update the book
    book["title"] = request.json.get("title", book["title"])
    book["author"] = request.json.get("author", book["author"])
    # Return the updated book
    return jsonify(book)


@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    """
    Delete a single book by ID.

    Args:
        book_id (int): The ID of the book to delete.

    Returns:
        dict: A message indicating that the book has been deleted, or a 404 error
            if the book is not found.
    """
    # Find the book by ID
    book = next((book for book in books if book["id"] == book_id), None)
    # If the book is not found, return a 404 error
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    # Otherwise, delete the book
    books.remove(book)
    # Return the message
    return jsonify({"message": "Book deleted"})


if __name__ == "__main__":
    app.run(debug=True)

