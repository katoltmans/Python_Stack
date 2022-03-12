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
def add_author():
    pass

# Route to view individual author info
@app.route("/authors/<int:num>")
def view_author():
    pass

# Route to add an author's favorite book
@app.route("/authors/add_book", methods=["POST"])
def favorite_book():
    pass




