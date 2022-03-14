from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book
from flask import flash

db = 'dojo_survey_schema'

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # create
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES ( %(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW() );"
        return connectToMySQL(db).query_db(query, data)
    
    # read
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(db).query_db(query)
        all_dojos = []
        for row in results:
            all_dojos.append( cls(row) )
        return all_dojos
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    # update
    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET name = %(name)s, location = %(location)s, language = %(language)s, comment = %(comment)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
    
    # delete
    def delete(cls, data):
        query = "DELETE * FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
    
    @staticmethod
    def validate_survey(data):
        is_valid = True # we assume this is true
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(data['location']) < 1:
            flash("Location is a required field.")
            is_valid = False
        if len(data['language']) < 1:
            flash("Language is a required field.")
            is_valid = False
        if len(data['comment']) < 3:
            flash("Comment must be at least 3 characters.")
            is_valid = False
        return is_valid