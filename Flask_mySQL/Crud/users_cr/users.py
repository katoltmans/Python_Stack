# Import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL

# Create users class after users table in database
class Users:
    def __init__(self, user):
        self.id = user['id']
        self.first_name = user['first_name']
        self.last_name = user['last_name']
        self.email = user['email']
        self.created_at = user['created_at']
        self.updated_at = user['updated_at']
        
    # Create get_all class method to display users
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # Connect to schema
        results = connectToMySQL("users").query_db(query)
        # Create empty list to append
        users = []
        # Iterate through db results
        for user in results:
            users.append( cls(user))
        return users
    
    # Create add_new method to add a new user
    @classmethod
    def add_new(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        return connectToMySQL("users").query_db(query, data)
    
    # Method to view user info
    @classmethod
    def view_user(cls, num):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL("users").query_db(query, data = {"id": num})
        # cls = self - passes in the latest accessed row in the query
        print(results)
        return cls(results[0])
    
    # Edit a user's information
    @classmethod
    def edit(cls, data):
        query = "UPDATE users set name="