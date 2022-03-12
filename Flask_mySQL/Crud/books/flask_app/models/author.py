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
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
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
    
    # Method to display one author 
    @classmethod
    def view_favorite_books_of_author(cls, data):
        # LEFT JOINS needed since this is a many to many relationship
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)
        if len(results) == 0:  # No books are registered
            return None
        else:
            this_author = cls(results[0])
            for row_from_db in results:
            # Book data to display
                book_data = {
                    "id": row_from_db['books.id'],
                    "title": row_from_db['title'],
                    "num_of_pages": row_from_db['num_of_pages'],
                    "created_at": row_from_db['books.created_at'],
                    "updated_at": row_from_db['books.updated_at']
                }
                this_author.books.append( book.Book(book_data) )
            return this_author
        