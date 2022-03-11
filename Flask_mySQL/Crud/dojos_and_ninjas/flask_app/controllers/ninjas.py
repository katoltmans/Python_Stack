from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import ninja # Create dojos with ninja.Ninja()

# Route to add a ninja
@app.route("/ninjas", methods=["POST"])
def add_ninja():
    pass

# Route display add ninja form
@app.route("/ninjas/new")
def display_add_ninja():
    return render_template("/add_ninja.html")




