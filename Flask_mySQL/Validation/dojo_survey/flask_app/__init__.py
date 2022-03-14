#Imports, instance creation and secret key
from flask import Flask
app = Flask(__name__)
app.secret_key = "youwereneverhere"