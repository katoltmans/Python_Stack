from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)  # Set bcrypt function as a variable and invoke the function
import re

class User:
    # Assign the schema
    schema = "recipes_schema"
    
    # Create the regular expression used to validate emails
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    PASSWORD_REGEX = re.compile(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,32}$')
    
    def __init__(self, data):  # Attributes of the user class
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        #self.users = []
    
    # Method to create a user
    @classmethod
    def new_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) \
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
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
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)
        # Action when no matching email is found
        if len(results) <1:  # Can also do ==0?
            return False
        return cls(results[0])
        

    
    # Method to check password of user
    @classmethod
    def check_password(cls, data):
        pass
    
    # Static method to diplay flash messages for registration
    def validate_registration(form_data):
        is_valid = True
        print(form_data['first_name'] + str(len(form_data['first_name'])))
        if len(form_data['first_name']) < 2:
            print("First name too short")
            flash("Need at least 2 characters in your first name, Chef.", "register")
            is_valid = False
        if len(form_data['last_name']) < 2:
            flash("Need at least 2 characters in your last name, Chef.", "register")
            is_valid = False
        # Compare input to regex
        if not User.EMAIL_REGEX.match(form_data['email']):
            flash("Invalid email address.  Arr, try again matey!", "register")
            is_valid = False
        # Check for repeat emails
        if User.has_repeats(form_data):
            flash("Email already exists. Give 'er another shot!", "register")
            is_valid = False
        if not User.PASSWORD_REGEX.match(form_data['password']):
            flash("Chefs require the utmost security. Please use a password with 8-32 characters and at least 1 uppercase letter, and 1 number.", "register")
            is_valid = False
        #Confirm if reentered password matches
        if form_data['confirm_password'] != form_data['password']:
            flash("Sorry Chef, passwords must match.", "register")
            is_valid = False
        return is_valid
    
    # Static method to diplay flash messages for login
    def validate_login(form_data, user_in_db):
        is_valid = True
        if user_in_db == False:
            print("Invalid email")
            is_valid = False
        # Check to see if password matches
        if not bcrypt.check_password_hash(user_in_db.password, form_data['password']):
            print("Invalid password")
            is_valid = False
        # If either credential is false, print flash message
        if not is_valid:
            flash("Invalid credentials", "login")
        return is_valid