from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    """Return a simple hello world message

    This is just a simple route to test that the Flask app is working
    correctly. It returns a plain text "Hello, World!" message.
    """
    # Return a simple HTML page with a "Hello, World!" message
    return "<p>Hello, World!</p>"
