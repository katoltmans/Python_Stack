from flask_app import app # import the app
from flask_app.controllers import authors, books  #import controllers

if __name__=="__main__":
    app.run(debug=True)