from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import user

class Message:
    # Assign schema
    schema = "private_wall_schema"
    
    def __init__(self, data):
        self.id = data["id"]
        self.message = data["message"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.sender = None
    
    # Method to create a message
    def create_message(cls, data):
        pass
    
    # Method to display messages
    def display_messages(cls, data):
        pass
    
    # Method to like a message
    def like_message(cls, data):
        pass
    
    # Method to delete a message
    def delete_message(cls, data):
        pass
        