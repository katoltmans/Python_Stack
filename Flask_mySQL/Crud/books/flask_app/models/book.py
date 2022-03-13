from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Book:
    schema = "books"  # Declare schema variable
    
    def __init__(self, data): #attributes of the Book class
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #List to add authors later
        self.authors = []
    
    #Method to add a book
    @classmethod
    def new_book(cls, data):
        pass
    
    #Method to display books page
    @classmethod
    def display_books(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL(cls.schema).query_db(query)
        print(results)
        all_books = []  # List to hold all books
        for one_book in results:
            book_instance = cls(one_book)  # Create an instance of an book
            all_books.append(book_instance) # Add an book to the list
        return all_books
    