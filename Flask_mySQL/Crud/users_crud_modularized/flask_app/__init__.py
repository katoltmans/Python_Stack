from flask import Flask
app = Flask(__name__) # Create the app

app.secret_key = "noneshallpass"
