from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
import re

class Recipe:
    # Assign the schema
    schema = "recipes_schema"
    
    def __init__(self, data):  # Attributes of the user class
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_made = data["date_made"]
        self.under_30 = data["under_30"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.recipes = []
    
    # Method to create a recipe
    @classmethod
    def new_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_30, created_at, updated_at) \
        VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s,, %(under_30)s NOW(), NOW());"
        results = connectToMySQL(cls.schema).query_db(query, data)
        print(results)
        return results
    
    # Method to display all recipes
    @classmethod
    def display_recipes(cls):
        query = "Select * from recipes WHERE recipes.id = %(id)s;"
        results = connectToMySQL(cls.schema).query_db(query)
        print(results)
        all_recipes = [] # List to hold all recipes
        if not results or len(results) == 0:  # No recipes are registered to a user
            return None
        for one_recipe in results:
            all_recipes.append(cls(one_recipe))  # Add a recipe to the list
        return all_recipes
    
    # Method to display one recipe 
    @classmethod
    def view_one_recipe(cls, data):
        # LEFT JOINS needed since this is a many to many relationship
        query = "SELECT * FROM recipes LEFT JOIN users_has_recipes ON users_has_recipes.recipe_id = recipes.id LEFT JOIN users ON users_has_recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)
        if len(results) == 0:  # No books are registered
            return None
        else:
            this_recipe = cls(results[0])
            for row_from_db in results:
            # User data to join
                user_data = {
                    "id": row_from_db['users.id'],
                    "first_name": row_from_db['first_name'],
                    "last_name": row_from_db['last_name'],
                    "email": row_from_db['email'],
                    "created_at": row_from_db['authors.created_at'],
                    "updated_at": row_from_db['authors.updated_at']
                }
                this_recipe.users.append( user.User(user_data) )
            return this_recipe