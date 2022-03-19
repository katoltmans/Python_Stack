from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)  # Set bcrypt function as a variable and invoke the function
from flask import render_template, redirect, request, session
from flask_app.models import user

# Route to display redister/login page
@app.route("/")
def display_login():
    return render_template("login.html")

# Route to process registration data
@app.route("/register", methods=["POST"])
def process_registration():
    # Redirect home if not a valid email
    if not user.User.validate_registration(request.form):
        return redirect("/")
    # Create the hash of the password
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    pw_hash_confirm = bcrypt.generate_password_hash(request.form["confirm_password"])
    print(pw_hash)
    print(pw_hash_confirm)
    # Create an user dictionary
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash,
        "confirm_password": pw_hash_confirm
    }
    # Call the new_user method to add the user to the database
    user_id = user.User.new_user(data)
    # Save session info
    session['first_name'] = request.form["first_name"]
    session['id'] = user_id
    # call new_user method
    return redirect("/dashboard")

# Route to process login
@app.route("/login", methods=["POST"])
def process_login():
    # Check to see if the email exists
    email_data = {
        "email": request.form["email"]
    }
    user_in_db = user.User.get_by_email(email_data)
    # Redirect home if not a valid email
    if not user.User.validate_login(request.form, user_in_db):
        return redirect("/")
    # Save session info
    session['id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name 
    # Redirect to the user's dashboard
    return redirect("/dashboard")

# Route to display dashboard
@app.route("/dashboard")
def display_dashboard():
    # Check to see if the user is in session
    if "id" not in session:
        return redirect("/")
    # Data to display the user's first name
    data = {"id": session['id']}
    return render_template("dashboard.html", one_user = user.User.display_user(data))

# Route to logout
@app.route("/logout")
def process_logout():
    session.clear()
    return redirect("/")