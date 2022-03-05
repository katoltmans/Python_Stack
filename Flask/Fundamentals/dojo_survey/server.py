#Imports, instance creation and secret key
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "youwereneverhere"

#Route to display homepage
@app.route("/")
def blankSurvey():
    return render_template("index.html")


#Route to process input info
@app.route("/process", methods=["POST"])
def processUser():
    #print(request.form)
    session['name'] = request.form["name"]
    session['location'] = request.form["location"]
    session['language'] = request.form["language"]
    session['comments'] = request.form["comments"]
    return redirect("/result")

#Route to display input results
@app.route("/result")
def displayResults():
    return render_template("results.html")

if __name__=="__main__":
    app.run(debug=True)