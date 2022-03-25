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
        self.sender = None  #Messages are written by one sender
    
    # Method to create a message
    @classmethod
    def create_message(cls, data):
        query = """INSERT INTO messages (message, created_at, updated_at, users_id) 
        VALUES (%(message)s, NOW(), NOW(), %(users_id)s);"""
        results = connectToMySQL(cls.schema).query_db(query, data)
        print(results)
        return results
    
    # Method to display messages
    @classmethod
    def display_messages_by_sender(cls, data):
        query='''SELECT * FROM messages 
        LEFT JOIN friendships ON friendships.user2_id = messages.users_id 
        LEFT JOIN users ON users.id = friendships.user2_id 
        WHERE user_id = %(id)s;'''
        results = connectToMySQL(cls.schema).query_db(query, data)
        all_messages = []
        # Check if there are any messages
        if len(results) < 1:
            return None
        else:
            for row_in_db in results:
                # Create an instance of a message
                one_message = cls(row_in_db)
                # Sender (user2) class instance
                one_message_sender_info = {
                    "id": row_in_db["users.id"],
                    "first_name": row_in_db["first_name"],
                    "last_name": row_in_db["last_name"],
                    "email": row_in_db["email"],
                    "password": row_in_db["password"],
                    "created_at": row_in_db["users.created_at"],
                    "updated_at": row_in_db["users.updated_at"]
                }
                # Create a sender instance in the User class
                message_writer = user.User(one_message_sender_info)
                # Associate the message with the sender
                one_message.sender = message_writer
                # Append the message and sender to the list of messages
                all_messages.append(one_message)
            return all_messages
                
            
    # Method for message count
    @classmethod
    def message_count(cls, data):
        query='''SELECT COUNT(*) AS count FROM messages 
        LEFT JOIN friendships ON friendships.user2_id = messages.users_id 
        LEFT JOIN users ON users.id = friendships.user2_id 
        WHERE user_id = %(id)s;'''
        results = connectToMySQL(cls.schema).query_db(query, data)
        count = results[0]["count"]
        print(results)
        return str(count)
    
    # Method to like a message
    @classmethod
    def like_message(cls, data):
        pass
    
    # Method to delete a message
    @classmethod
    def delete_message(cls, data):
        pass
    
    # Static method to check for validations
    @staticmethod
    def validate_messages(form_data):
        is_valid = True
        print(form_data)
        # Check to make sure messages are at least 5 characters long
        if len(form_data["message"]) < 5 :
            print("Message too short")
            flash("All messages must be at least 5 characters long", "message_sent")
            is_valid = False
        return is_valid