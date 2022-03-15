from mysqlconnection import connectToMySQL
from flask import flash
import re

# Create the regular expression used to validate emails
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class EmailModel:
    schema = "email_validation"
    
    def __init__(self, data):  # Attributes of email class
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.emails = []
    
    # Method to create an email
    @classmethod
    def new_email(cls, data):
        query = "INSERT INTO email (email) VALUES (%(email)s);"
        results = connectToMySQL(cls.schema).query_db(query, data)
        print(results)
        return results
    
    # Method to display all emails
    @classmethod
    def display_emails(cls):
        query = "SELECT * FROM email;"
        results = connectToMySQL(cls.schema).query_db(query)
        print(results)
        all_emails = []
        for one_email in results:
            email_instance = cls(one_email) # Create an instance of an email
            all_emails.append(email_instance)  # Add to email list
        return all_emails
    
    # Method to get one email
    @classmethod
    def get_one_email(cls, data):
        query = "SELECT * FROM email WHERE email.id = %(id)s;"
        results = connectToMySQL(cls.schema).query_db(query)
        print(results)
        if len(results)==0:
            return None
        else:
            return cls(results[0])
    
    # Method to delete an email
    @classmethod
    def delete_email(cls, data):
        query = "DELETE FROM email WHERE email.id = %(id)s;"
        return connectToMySQL(cls.schema).query_db(query, data)
    
    # Method to check identify repeats
    @classmethod
    def has_repeats(cls, data):
        query = "SELECT COUNT(*) AS count FROM email WHERE email= %(email)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)
        print(results)
        return results[0]['count'] > 0
    
    # Static method to validate emails
    @staticmethod
    def validate_email(emailInput):
        is_valid = True
        # Compare input to regex
        if not EMAIL_REGEX.match(emailInput['email']):
            flash("Invalid email address.  Arr, try again matey!")
            is_valid = False
        # Check for repeat emails
        if EmailModel.has_repeats(emailInput):
            flash("Email already exists. Give 'er another shot!")
            is_valid = False
        return is_valid