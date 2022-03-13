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
def view_book_info(num):
    # Display one author with favorite books of author
    data = {
        "id": num
    }
    return render_template("view_book.html", one_book = book.Book.view_authors_who_favorited_book(data), all_authors = author.Author.display_authors())

# Route to favorite a book by an author
@app.route("/books/<int:num>/add_book", methods=["POST"])
def favorite_of_author_to_database(num):
    # Create a favorites dictionary
    data = {
        "author_id": request.form["author_id"],
        "book_id": num
    }
    author.Author.add_favorite_book(data)
    return redirect("/books/"+str(num))