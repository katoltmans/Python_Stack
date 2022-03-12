from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import author

# Route to redirect index page to /authors
@app.route("/")
def index():
    return redirect("/authors")

# Route to display authors page
@app.route("/authors")
def display_author_page():
    return render_template("authors.html", all_authors = author.Author.display_authors())

# Route to process add author input
@app.route("/authors/new", methods=["POST"])
def new_author():
    # Create an author dictionary
    data = {
        "name": request.form["name"]
    }
    # call new_author method
    author.Author.new_author(data)
    return redirect("/authors")

# Route to view individual author info with books
@app.route("/authors/<int:num>")
def view_author_info(num):
    # Display one author with favorite books of author
    data = {
        "id": num
    }
    return render_template("view_author.html", one_author = author.Author.view_favorite_books_of_author(data))

# Route to add an author's favorite book
@app.route("/authors/add_book", methods=["POST"])
def favorite_book():
    pass




