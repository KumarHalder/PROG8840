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
@app.route("/status")
def status():
    """Return the status of the application in JSON format.

    This is useful for health checks or providing basic metadata about the
    application.
    """
    return {
        "status": "running",
        "version": "1.0.0"
    }
@app.route("/greet/<name>")
def greet(name):
    """
    Greet the user with their name.

    The <name> part of the URL is captured and passed to the function.
    """
    return f"<p>Hello, {name}!</p>"
@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page."""
    return "<h1>404</h1><p>Sorry, the page you're looking for cannot be found.</p>", 404
