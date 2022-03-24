from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, message

# Route to display dashboard
@app.route("/wall")
def display_wall():
    # Check to see if the user is in session
    if "id" not in session:
        return redirect("/")
    # Data to display the user's first name
    data = {"id": session['id']}
    print("session" + str(session['id']))
    return render_template("wall.html", one_user = user.User.display_user(data)) #, \
        #all_recipes = recipe.Recipe.display_recipes(data))

#Route to process message data
@app.route("/wall/message/add", methods=["POST"])
def process_message_data():
    # Redirect if not valid
    
    # Create a message dictionary
    data = {
        "message": request.form["message"],
        "user_id": session["id"]
    }
    #Call the add message method
    message.Message.create_message(data)
    return redirect("/wall")

#Route to display warning page
@app.route("/danger", methods=["POST"])
def danger_message():
    pass

