from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import dojo, ninja # Create dojos with dojo.Dojo()

# home route - will reroute to /dojos
@app.route("/")
def index():
    return redirect("/dojos")

# Route to display dojos
@app.route("/dojos")
def all_dojos():
    return render_template("dojos.html", all_dojos = dojo.Dojo.display_all_dojos())

# Route to add a new dojo to the database
@app.route("/dojos/add", methods=["POST"])
def add_dojo():
    # Create a dojo dictionary
    data = { 
        "name": request.form["name"]
    }
    #Call on add_dojo classmethod
    dojo.Dojo.add_dojo(data)
    return redirect("/dojos")

# Route to view ninjas in dojo
@app.route("/dojos/<int:num>")
def view_dojo_info(num):
    # Display one dojo with it's ninjas
    data = {
        "id": num
    }
    return render_template("dojo_info.html", one_dojo = dojo.Dojo.display_one_dojo_with_ninjas(data), all_ninjas = ninja.Ninja.display_all_ninjas(data))