from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo

class Ninja:
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
