from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)  # Set bcrypt function as a variable and invoke the function
from flask import render_template, redirect, request, session
from flask_app.models import user, recipe

# Route to display add a new recipe page
@app.route("/recipes/new")
def display_add_new_recipe_page():
    # Check to see if the user is in session
    if "id" not in session:
        return redirect("/")
    return render_template("add_recipe.html")

# Route to process new recipe info
@app.route("/recipes/new/process", methods=["POST"])
def process_new_recipe():
    # Create a recipe dictionary
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_made": request.form["date_made"],
        "under_30": request.form["under_30"],
        "user_id": session["id"]
    }
    # call new_author method
    recipe.Recipe.new_recipe(data)
    return redirect("/dashboard")

# Route to view an existing recipe
@app.route("/recipes/view/<int:num>")
def view_recipe(num):
    # Check to see if the user is in session
    if "id" not in session:
        return redirect("/")
    # Data to display the user's first name
    data = {
        "id": session['id'],
        "first_name": session['first_name'],
        "recipe_id": num
        }
    return render_template("view_recipe.html", one_user = user.User.display_user(data), \
        this_recipe = recipe.Recipe.view_one_recipe(data))

# Route to display edit recipe page
@app.route("/recipes/edit/<int:num>")
def display_edit_recipe_page(num):
    # Check to see if the user is in session
    if "id" not in session:
        return redirect("/")
    # Data to display the user's first name
    data = {
        "id": session['id'],
        "first_name": session['first_name'],
        "recipe_id": num
        }
    return render_template("edit_recipe.html", \
        this_recipe = recipe.Recipe.view_one_recipe(data))

# Route to edit an existing recipe
@app.route("/recipes/process/<int:num>", methods=['POST'])
def edit_recipe(num):
    print("Got Post Info")
    print(request.form)
    data = {
        "id": num,
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_made": request.form["date_made"],
        "under_30": request.form["under_30"],
    }
    recipe.Recipe.edit(data)
    return redirect("/dashboard")

# Route to delete an existing recipe
@app.route("/recipes/delete")
def delete_recipe():
    pass