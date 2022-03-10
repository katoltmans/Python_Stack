from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.user import Users


# Route for home page
@app.route('/')
def home():
    return redirect('/users')

# Route to Add New User page
@app.route('/user/add', methods=['POST'])
def add_user():
    print("Got Post Info")
    print(request.form)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    Users.add_new(data)
    return redirect("/users")

@app.route('/user/new')
def display_add_user():
    return render_template("users_new.html")

# Route to View all users
@app.route('/users')
def display_users():
    print("Show users")
    print(request.form)
    users = Users.get_all()
    return render_template("users.html", all_users = users)

# Route to view individual user info
@app.route('/users/<int:num>/')
def view_user(num):
    user = Users.view_user(num)
    return render_template("user_display.html", user = user)

# Route to edit a user
@app.route('/users/edit', methods=['POST'])
def edit_user():
    print("Got Post Info")
    print(request.form)
    data = {
        "id": request.form['id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    Users.edit(data)
    return redirect("/users")

# Route to display edit user page
@app.route('/users/<int:num>/edit')
def display_edit(num):
    user = Users.view_user(num)
    return render_template("edit_user.html", user = user)

# Route to delete a user
@app.route('/users/<int:num>/delete')
def delete_user(num):
    Users.delete_user(num)
    return redirect("/users")