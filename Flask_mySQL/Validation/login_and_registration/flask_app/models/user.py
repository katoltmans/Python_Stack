from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)  # Set bcrypt function as a variable and invoke the function


class User:
    schema = "login_and_registration"
    
    def __init__(self, data):  # Attributes of the user class
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.birthdate = data["birthdate"]
        self.fav_language = data["fav_language"]
        self.student = data["student"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.users = []
    
    # Method to create a user
    @classmethod
    def new_user(cls, data):
        pass
    
    # Method to display a user
    @classmethod
    def display_user(cls):
        pass
    
    # Method to check password of user
    @classmethod
    def check_password(cls, data):
        pass
    
    # Static method to diplay flash messages for registration
    def validate_registration():
        pass
    
    # Static method to diplay flash messages for login
    def validate_login():
        pass