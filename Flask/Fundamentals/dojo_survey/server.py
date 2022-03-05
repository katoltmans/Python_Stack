#Imports, instance creation and secret key
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "youwereneverhere"

#Route to display homepage
@app.route('/')
def blankSurvey():
    return render_template("index.html")


#Route to process input info



#Route to display input results


if __name__=="__main__":
    app.run(debug=True)