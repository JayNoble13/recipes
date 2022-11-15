from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL

db="recipes_schema"

class Recipe:
    def __init__(self,data):
        self.id=data["id"]
        self.name=data["name"]
        self.description=data["description"]
        self.instruction=data["instruction"]
        self.time=data["time"]
        self.date_made=data["date_made"]
        self.user_id=data["user_id"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]

    @classmethod
    def create(cls,data):
        query= "INSERT INTO recipes (name, description, instruction, time, date_made, user_id) VALUES (%(name)s, %(description)s, %(instruction)s, %(time)s, %(date_made)s, %(user_id)s)"
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def update(cls, data):
        query="UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, time = %(time)s, date_made = %(date_made)s, user_id = %(user_id)s) WHERE id = %(id)s"
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_one(cls, data):
        query="SELECT * FROM recipes WHERE id = %(id)s"
        results= connectToMySQL(db).query_db(query,data)
        return cls(results[0])

    @classmethod
    def getall(cls, data):
        query="SELECT * FROM recipes"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query= "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL(db).query_db(query, data)