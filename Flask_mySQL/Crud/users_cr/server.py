from flask import Flask, render_template, request, redirect
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
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    return redirect("/users")

@app.route('/user/new')
def display_add_user():
    return render_template("users_new.html")

# Route to View all users
@app.route('/users')
def display_users():
    print("Show users")
    print(request.form)
    return render_template("users.html")

if __name__=="__main__":
    app.run(debug=True)