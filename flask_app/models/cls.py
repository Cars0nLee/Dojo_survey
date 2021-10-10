from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
class Surv:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def save_info(cls, data):
        query = "INSERT INTO dojos(name, location, language, comment) VALUES(%(name)s, %(location)s, %(language)s, %(comment)s)"
        return connectToMySQL("dojo_survey_schema").query_db(query, data)
    
    @classmethod
    def get_info(cls):
        query = "SELECT*FROM dojos ORDER BY id DESC"
        db_dojos = connectToMySQL("dojo_survey_schema").query_db(query)
        return Surv(db_dojos[0])
        


    @staticmethod
    def validate(survey):
        is_valid = True
        if len(survey["name"]) < 1:
            is_valid = False
            flash("Full Name Required")
        if len(survey["location"]) < 1:
            is_valid = False
            flash("Location Required")
        if len(survey["language"]) < 1:
            is_valid = False
            flash("Language Required")
        if len(survey["comment"]) < 3:
            is_valid = False
            flash("Comment Required")
        return is_valid