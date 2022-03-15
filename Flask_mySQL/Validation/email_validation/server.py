from flask import Flask, render_template, request, redirect, session
from emailModel import EmailModel
app = Flask(__name__)
app.secret_key = "noonecanknow"

# Route to diplay home page
@app.route("/")
def enter_email():
    return render_template("index.html")

# Route to process email input
@app.route("/process", methods=["POST"])
def process_email():
    # Redirect home if not a valid email
    if not EmailModel.validate_email(request.form):
        return redirect("/")
    # Redirect to success page if email is valid
    data = {
        "email": request.form["email"]
    }
    EmailModel.new_email(data)
    # Save Session object
    session['email'] = request.form["email"]
    # Redirect to success page
    return redirect("/success")


# Route to display success page
@app.route("/success")
def display_emails():
    return render_template("success.html", all_emails = EmailModel.display_emails())

# Route to delete an email
@app.route("/delete/<int:num>")
def delete_email(num):
    data = {
        "id": num
    }
    EmailModel.delete_email(data)
    return redirect("/success")

if __name__ == "__main__":
    app.run(debug=True)