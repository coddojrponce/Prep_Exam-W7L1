from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

class Item:
    DB = "exam_prep"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.price = data['price']
        self.img_url = data['img_url']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.owner=None 
        self.likes=[]
        
    # the save method will be used when we need to save a new friend to our database
    @classmethod
    def save(cls, data):
        query = """INSERT INTO items (name, description,price,img_url,user_id)
    		VALUES (%(name)s, %(description)s, %(price)s,%(img_url)s,1);"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result

    @classmethod
    def get_one(cls, item_id):
        query  = "SELECT * FROM items WHERE id = %(id)s;"
        data = {'id': item_id}
        result = connectToMySQL(cls.DB).query_db(query, data)
        if not result:
            return None
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM items
        LEFT JOIN users
        ON items.user_id = users.id
        ;
        
        """
        results = connectToMySQL(cls.DB).query_db(query)
        if not results:
            return []
        items = []
        for item in results:
            this_item = cls(item)
            data={
                "id":item["users.id"],
                "first_name":item["first_name"],
                "last_name":item["last_name"],
                "email":item["email"],
                "password":item["password"],
                "created_at":item["users.created_at"],
                "updated_at":item["users.updated_at"]
            }

            this_item.owner = User(data)
            items.append(this_item)


        return items
    
    @classmethod
    def update(cls,data):
        query = """UPDATE items 
                SET name=%(name)s,description=%(description)s,img_url=%(img_url)s, price=%(price)s 
                WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def delete(cls, id):
        query  = "DELETE FROM items WHERE id = %(id)s;"
        data = {"id": id}
        return connectToMySQL(cls.DB).query_db(query, data)