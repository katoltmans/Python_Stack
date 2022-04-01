from flask_app import app
from flask import render_template, redirect, request, jsonify
import requests
#Reserved for importing controllers

# Render template and create gitUser controller
@app.route("/")
def git_user_info():
    return render_template("index.html")

# Run the app here
if __name__=="__main__":
    app.run(debug=True)