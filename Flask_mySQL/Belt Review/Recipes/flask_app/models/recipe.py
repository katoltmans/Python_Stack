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
        self.user_id = data["user_id"]
    
    # Method to create a recipe
    @classmethod
    def new_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_30, user_id, created_at, updated_at) \
        VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s, NOW(), NOW());"
        results = connectToMySQL(cls.schema).query_db(query, data)
        print(results)
        return results
    
    # Method to display all recipes
    @classmethod
    def display_recipes(cls, data):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.schema).query_db(query, data)
        all_recipes = []
        if not results or len(results) == 0:  # No books are registered
            return None
        else:
            for row_from_db in results:
                #Create a recipe name instance
                one_recipe = cls(row_from_db)
                # Add recipe to the recipe list
                all_recipes.append(one_recipe)
        return all_recipes
    
    # Method to display one recipe 
    @classmethod
    def view_one_recipe(cls, data):
        query = "Select * from recipes WHERE id = %(recipe_id)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)
        print(results)
        this_recipe = cls(results[0])
        return this_recipe
    
    # Edit a recipe's information
    @classmethod
    def edit(cls, data):
        query = "UPDATE recipes set name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s, under_30=%(under_30)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(cls.schema).query_db(query, data)
    
    # Method to delete a recipe
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id=%(id)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)
        print(results)
        return results
    
    # Static method to diplay flash messages for recipe entries
    def validate_recipe(form_data):
        is_valid = True
        print(form_data['name'] + str(len(form_data['name'])))
        if len(form_data['name']) < 3:
            print("Recipe name is too short")
            flash("Need at least 3 characters in your recipe name, Chef.", "recipe")
            is_valid = False
        if len(form_data['description']) < 3:
            print("Recipe description is too short")
            flash("Need at least 3 characters in your recipe description, Chef.", "recipe")
            is_valid = False
        if len(form_data['instructions']) < 3:
            print("Recipe instructions are too short")
            flash("Need at least 3 characters in your recipe instructions, Chef.", "recipe")
            is_valid = False
        return is_valid