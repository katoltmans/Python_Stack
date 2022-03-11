from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import dojo # Create dojos with dojo.Dojo()

# home route - will reroute to /dojos
@app.route("/")
def index():
    return redirect("/dojos")

# Route to display dojos and add new
@app.route("/dojos")
def all_dojos():
    return render_template("dojos.html")