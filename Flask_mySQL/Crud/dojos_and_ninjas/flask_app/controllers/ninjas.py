from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import ninja, dojo # Create dojos with ninja.Ninja()

# Route to add a ninja
@app.route("/ninjas/new", methods=["POST"])
def add_ninja():
    # Create ninja dictionary
    data = {  
        "dojo_id": request.form["dojo_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"]
    }
    # Call the function
    ninja.Ninja.add_ninja(data)
    return redirect("/dojos")
    

# Route display add ninja form
@app.route("/ninjas")
def display_add_ninja():
    return render_template("/add_ninja.html", all_dojos = dojo.Dojo.display_all_dojos())




