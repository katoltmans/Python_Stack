from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import author, book

# Route to display books page
@app.route("/books")
def display_books_page():
    return render_template("books.html", all_books = book.Book.display_books())

# Route to add a new book
@app.route("/books/add", methods=["POST"])
def add_book():
    # Create a book dictionary
    data = {
        "title": request.form["title"],
        "num_of_pages": request.form["num_of_pages"]
    }
    # call new_author method
    book.Book.new_book(data)
    return redirect("/books")

# Route to view individual book info
@app.route("/books/<int:num>")
def view_book():
    pass

# Route to favorite a book by an author
@app.route("/books/add_book", methods=["POST"])
def favorite_of():
    pass