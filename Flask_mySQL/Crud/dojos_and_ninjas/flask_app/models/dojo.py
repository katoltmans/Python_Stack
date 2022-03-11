from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

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
    
    #Method to display ninjas in a dojo
    @classmethod
    def display_one_dojo_with_ninjas(cls, data):
        # LEFT JOIN since the dojo_id is on ninjas
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)
        if len(results) == 0:  # No ninjas are registered
            return None
        else:
            this_dojo = cls(results[0])
            # Grab data for ninja
            ninja_data = {
                "id": results[0]['ninjas.id'],
                "first_name": results[0]['first_name'],
                "last_name": results[0]['last_name'],
                "age": results[0]['age'],
                "created_at": results[0]['ninjas.created_at'],
                "updated_at": results[0]['ninjas.updated_at'],
                "dojo_id": results[0]['dojo_id'],
            }
        these_ninjas = ninja.Ninja(ninja_data) # Create the ninja
        this_dojo.ninja = these_ninjas  # Link the ninja to the dojo
        return this_dojo
