from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)  # Set bcrypt function as a variable and invoke the function
import re

class User:
    # Assign the schema
    schema = "login_and_registration"
    
    # Create the regular expression used to validate emails
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    PASSWORD_REGEX = re.compile(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,32}$')
    
    def __init__(self, data):  # Attributes of the user class
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.birthdate = data["birthdate"]
        self.fav_language = data["fav_language"]
        self.student = data["student"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        #self.users = []
    
    # Method to create a user
    @classmethod
    def new_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, birthdate, fav_language, student, password, created_at, updated_at) \
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(birthdate)s, %(fav_language)s, %(student)s, %(password)s, NOW(), NOW());"
        results = connectToMySQL(cls.schema).query_db(query, data)
        print(results)
        return results
    
    # Method to display a user
    @classmethod
    def display_user(cls, data):
        query = "Select * from users WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)
        print(results)
        if len(results) == 0:  # No users are registered
            return None
        this_user = cls(results[0])
        return this_user
    
    # Method to check identify repeats
    @classmethod
    def has_repeats(cls, data):
        query = "SELECT COUNT(*) AS count FROM users WHERE email= %(email)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)
        print(results)
        return results[0]['count'] > 0
    
    # Method to check if a user's email is in the database
    @classmethod
    def get_by_email(cls, data):
        pass
    
    # Method to check password of user
    @classmethod
    def check_password(cls, data):
        pass
    
    # Static method to diplay flash messages for registration
    def validate_registration(user):
        is_valid = True
        print(user['first_name'] + str(len(user['first_name'])))
        if len(user['first_name']) < 2:
            print("First name too short")
            flash("Need at least 2 characters in your first name, ninja.", "register")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Need at least 2 characters in your last name, ninja.", "register")
            is_valid = False
        # Compare input to regex
        if not User.EMAIL_REGEX.match(user['email']):
            flash("Invalid email address.  Arr, try again matey!", "register")
            is_valid = False
        # Check for repeat emails
        if User.has_repeats(user):
            flash("Email already exists. Give 'er another shot!", "register")
            is_valid = False
        if not User.PASSWORD_REGEX.match(user['password']):
            flash("Ninjas require the utmost security. Please use a password with 8-32 characters and at least 1 uppercase letter, and 1 number.", "register")
            is_valid = False
        #Confirm if reentered password matches
        if user['confirm_password'] != user['password']:
            flash("Sorry ninja, passwords must match.", "register")
            is_valid = False
        return is_valid
    
    # Static method to diplay flash messages for login
    def validate_login(user):
        is_valid = True
        # Compare input to regex
        if not User.EMAIL_REGEX.match(user['email']):
            flash("Invalid email address.  Arr, try again matey!", "login")
            is_valid = False
        
        #print("Invalid password")
        #flash("Sorry ninja, your password appears to be incorrect.")
        #is_valid = False
        return is_valid