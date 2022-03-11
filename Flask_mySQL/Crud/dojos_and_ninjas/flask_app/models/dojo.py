from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    schema = "dojos_and_ninjas" # declare schema variable
    
    def __init__(self, data): # dojo class attributes
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojos = []  # Dictionary to contain added dojos
    
    # Dojo classmethods
    
    # Method to add a dojo
    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        results = connectToMySQL(cls.schema).query_db(query, data)
        print(results)
        return results
    
    
    # Method to display dojos
    @classmethod
    def display_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.schema).query_db(query)
        print(results)
        all_dojos = [] # list will hold instances of the dojos class
        for one_dojo in results:
            dojo_instance = cls(one_dojo) # Create an instance of a dojo
            all_dojos.append(dojo_instance) #add dojo to the list of dojos
        return all_dojos