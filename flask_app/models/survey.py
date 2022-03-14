from flask_app.config.mysqlconnection import connectToMySQL
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
        query = "INSERT INTO surveys (name, location, language, comment, created_at, updated_at) VALUES ( %(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW() );"
        return connectToMySQL(db).query_db(query, data)
    
    # read
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM surveys;"
        results = connectToMySQL(db).query_db(query)
        all_surveys = []
        for row in results:
            all_surveys.append( cls(row) )
        return all_surveys
    
    @classmethod
    def get_last(cls):
        query = "SELECT * FROM surveys ORDER BY surveys.id DESC LIMIT 1;"
        results = connectToMySQL(db).query_db(query)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate_survey(survey):
        is_valid = True # we assume this is true
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(survey['location']) < 3:
            flash("Location is a required field.")
            is_valid = False
        if len(survey['language']) < 3:
            flash("Language is a required field.")
            is_valid = False
        if len(survey['comment']) < 3:
            flash("Comment must be at least 3 characters.")
            is_valid = False
        return is_valid