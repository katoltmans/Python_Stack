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
        self.creator = None
    
    # Method to create a recipe
    @classmethod
    def new_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_30, user_id, created_at, updated_at) \
        VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s, NOW(), NOW());"
        results = connectToMySQL(cls.schema).query_db(query, data)
        print(results)
        return results
    
    # Method to display one recipe 
    @classmethod
    def view_one_recipe(cls, data):
        query = "Select * from recipes WHERE recipes.id = %(id)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)
        print(results)
        all_recipes = [] # List to hold all recipes
        if not results or len(results) == 0:  # No recipes are registered to a user
            return None
        for one_recipe in results:
            all_recipes.append(cls(one_recipe))  # Add a recipe to the list
        return all_recipes
    
    # Method to display all recipes
    @classmethod
    def display_recipes(cls, data):
        # JOIN only needed since this is a one to many relationship
        query = "SELECT * FROM recipes WHERE user_id = %(id)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)
        all_recipes = []
        if not results or len(results) == 0:  # No books are registered
            return None
        else:
            for row_from_db in results:
                #Create a recipe name instance
                one_recipe = cls(row_from_db)
                # User data to join
                all_recipes.append(one_recipe)
        return all_recipes