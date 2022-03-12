from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    schema = "books"  # Declare schema variable
    
    def __init__(self, data): # Attributes of the Author class
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #List to add books later
        self.books = []
    
    # Method to add an author
    @classmethod
    def new_author(cls, data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        results = connectToMySQL(cls.schema).query_db(query, data)
        print(results)
        return results
    
    # Method to display authors page
    @classmethod
    def display_authors(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL(cls.schema).query_db(query)
        print(results)
        all_authors = []  # List to hold all authors
        for one_author in results:
            author_instance = cls(one_author)  # Create an instance of an author
            all_authors.append(author_instance) # Add an author to the list
        return all_authors
    
    