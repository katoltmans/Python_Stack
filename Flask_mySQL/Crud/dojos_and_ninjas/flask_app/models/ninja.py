from flask_app.config.mysqlconnection import connectToMySQL  #Connect to MySQL
from flask_app.models import dojo # Import dojo model

class Ninja:
    schema = "dojos_and_ninjas" # declare schema variable
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    
    # Method to save ninja info
    @classmethod
    def save( cle, data ):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at) VALUES "

    # Method to add a ninja
    @classmethod
    def add_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, (%(last_name)s, (%(age)s, (%(dojo_id)s;"
        return connectToMySQL(cls.schema).query_db(query, data)