from flask_app.config.mysqlconnection import connectToMySQL

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