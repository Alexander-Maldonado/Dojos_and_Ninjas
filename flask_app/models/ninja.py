from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results =connectToMySQL("dojos_and_ninjas").query_db(query)
        ninjas = []
        for n in results:
            ninjas.append( cls(n) )
        return ninjas

    @classmethod
    def get_one(cls, data):
        query = "Select * from ninjas WHERE id =%(id)s;"
        results =connectToMySQL("dojos_and_ninjas").query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, Dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(Dojo_id)s;);"
        result = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        return result

    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE ninjas.id = %(id)s;"
        return connectToMySQL("dojos_and_ninjas").query_db(query, data)


    @classmethod
    def delete(cls,data):
        query = "Delete from ninjas WHERE id = %(id)s;"
        return connectToMySQL("dojos_and_ninjas").query_db(query, data)