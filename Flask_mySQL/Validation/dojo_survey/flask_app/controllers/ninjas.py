from flask_app import app  # Import the app
from flask import render_template, request, redirect, session
from flask_app.models import ninja

#Route to display homepage
@app.route("/")
def blankSurvey():
    return render_template("index.html")


#Route to process input info
@app.route("/process", methods=["POST"])
def processNinja():
    #print(request.form)
    data = {
        "name": request.form["name"],
        "location": request.form["location"],
        "language": request.form["language"],
        "comment": request.form["comment"]
    }
    
    # Redirect home if there are errors in input
    if not ninja.Ninja.validate_ninja(request.form):
        return redirect('/')
    
    
    # process form if there are no errors
    # Call new_ninja method
    num = ninja.Ninja.new_ninja(data)
    return redirect("/result/" + str(num))

#Route to display input results
@app.route("/result/<int:num>")
def displayResults(num):
    data = {
        "id": num
    }
    return render_template("results.html", one_ninja = ninja.Ninja.display_ninja_data(data))