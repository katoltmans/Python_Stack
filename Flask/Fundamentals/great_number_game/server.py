#Import Flask
from flask import Flask, render_template
app = Flask(__name__)
#app.secret_key = "None shall pass"

#Routes
#Home page route
@app.route('/')
def home_page():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)