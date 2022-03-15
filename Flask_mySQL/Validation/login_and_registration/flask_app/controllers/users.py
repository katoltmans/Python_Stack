from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)  # Set bcrypt function as a variable and invoke the function
from flask import render_template, redirect, request, session
from flask_app.models.user import User

# Route to display redister/login page
@app.route("/")
def display_login():
    return render_template("login.html")

# Route to process registration data
@app.route("/register", methods=["POST"])
def process_registration():
    pass

# Route to process login
@app.route("/login", methods=["POST"])
def process_login():
    pass

# Route to display dashboard
@app.route("/dashboard")
def display_dashboard():
    pass

# Route to logout
@app.route("/logout")
def process_logout():
    pass

