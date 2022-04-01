from flask import Flask
app = Flask(__name__) # Create the app

app.secret_key = "apipracticetime" # Needed for session and flash messages 