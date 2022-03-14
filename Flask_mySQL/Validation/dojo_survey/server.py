from flask_app import app  # Import app
from flask_app.controllers import ninjas  # Import controller

if __name__=="__main__":
    app.run(debug=True)