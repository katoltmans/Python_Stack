from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import author

# Route to display books page
@app.route("/books")
def display_books_page():
    pass

# Route to add a new book
@app.route("/books/add")
def add_book():
    pass

# Route to view individual book info
@app.route("/books/<int:num>")
def view_book():
    pass

# Route to favorite a book by an author
@app.route("/books/add_book", methods=["POST"])
def favorite_of():
    pass