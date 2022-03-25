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
    all_messages = message.Message.display_messages_by_sender(data)
    return render_template("wall.html", one_user = user.User.display_user(data), \
        all_friends = user.User.get_friends(data), \
            all_messages = all_messages, \
                message_count = len(all_messages), \
                    sent_count = message.Message.message_count(data))


#Route to process message data
@app.route("/wall/message/add", methods=["POST"])
def process_message_data():
    # Check to see if the user is in session
    if "id" not in session:
        return redirect("/")
    # Redirect if not valid
    if not message.Message.validate_messages(request.form):
        return redirect("/wall")
    # Create a message dictionary
    data = {
        "message": request.form["message"],
        "users_id": session["id"],
    }
    print(data)
    #Call the add message method
    message.Message.create_message(data)
    return redirect("/wall")

#Route to delete message
@app.route("/delete/<int:num>")
def delete_message(num):
    # Check to see if the user is in session
    if "id" not in session:
        return redirect("/danger")
    else:
        data = {
            "id": num
        }
        message.Message.delete_message(data)
    return redirect("/wall")

#Route to display warning page
@app.route("/danger")
def danger_message():
    return render_template("danger.html")
    