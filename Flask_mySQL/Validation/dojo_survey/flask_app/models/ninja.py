from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Ninja:
    schema = "dojo_survey_schema"  # Declare schema variable
    
    def __init__(self, data):  # Attributes of the dojo class
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
    # Method to create a ninja in a dojo
    @classmethod
    def new_ninja(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        results = connectToMySQL(cls.schema).query_db(query, data)
        print(results)
        return results
    
    # Method to diplay entered ninja data
    @classmethod
    def display_ninja_data(cls, data):
        query = "SELECT * from dojos WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)
        print(results)
        if len(results) == 0:  # No ninjas registered
            return None
        else:
            this_ninja = cls(results[0])
            
        return this_ninja
    
    # Static method to validate inputs
    @staticmethod
    def validate_ninja(ninja):
        is_valid = True  # Assume state is true
        if len(ninja['name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(ninja['location']) < 2:
            flash("Please select a location.")
            is_valid = False
        if len(ninja['language']) < 2:
            flash("Please select a language.")
            is_valid = False
        if len(ninja['comment']) < 3:
            flash("Comment must be at least 3 characters.")
            is_valid = False
        return is_valid