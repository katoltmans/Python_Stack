from flask import Flask, render_template, request, redirect
from users import Users
app = Flask(__name__)

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
@app.route('/users/<int:num>/edit')
def edit_user(num):
    pass


# Route to delete a user
@app.route('/users/<int:num>/delete')
def delete_user(num):
    pass

if __name__=="__main__":
    app.run(debug=True)