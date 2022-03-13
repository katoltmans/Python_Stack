from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

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
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());"
        results = connectToMySQL(cls.schema).query_db(query, data)
        print(results)
        return results
    
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
    
    # Method to display one book 
    @classmethod
    def view_authors_who_favorited_book(cls, data):
        # LEFT JOINS needed since this is a many to many relationship
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)
        if len(results) == 0:  # No books are registered
            return None
        else:
            this_book = cls(results[0])
            for row_from_db in results:
            # Book data to display
                author_data = {
                    "id": row_from_db['authors.id'],
                    "name": row_from_db['name'],
                    "created_at": row_from_db['authors.created_at'],
                    "updated_at": row_from_db['authors.updated_at']
                }
                this_book.authors.append( author.Author(author_data) )
            return this_book
        
    # Method to display who have not favorited a book 
    @classmethod
    def view_authors_who_have_not_favorited_book(cls, data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN (SELECT author_id from favorites WHERE book_id =  %(id)s);"
        results = connectToMySQL(cls.schema).query_db(query, data)
        if len(results) == 0:  # No books are registered
            return None
        else:
            authors = []
            for row_from_db in results:
            # Book data to display
                author_data = {
                    "id": row_from_db['id'],
                    "name": row_from_db['name'],
                    "created_at": row_from_db['created_at'],
                    "updated_at": row_from_db['updated_at']
                }
                authors.append( author.Author(author_data) )
            return authors
    