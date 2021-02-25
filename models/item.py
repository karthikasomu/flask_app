# import sqlite3
from db import db
class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision = 2))



    def __init__(self,name,price):
        self.name = name
        self.price = price

    def json(self):
        return {'name':self.name,'price':self.price}

    @classmethod
    def find_by_name(cls,name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "select * from items where name = ?"
        # result = cursor.execute(query,(name,))
        # row = result.fetchone()

        # if row:
        #     return cls(row[0],row[1])
        # res = cls.query.filter_by(name = name)
        # print(f"res: {res}")
        return cls.query.filter_by(name = name).first()


    
    def save_to_db(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "insert into items values(?,?)"
        # cursor.execute(query,(self.name,self.price,))
        # connection.commit()
        # connection.close()
        db.session.add(self)
        db.session.commit()

    #for sqlalchemy both the update and insert are same

    # def update(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #     query = "update items set price =? where name =?"
    #     cursor.execute(query,(self.price,self.name,))
    #     connection.commit()
    #     connection.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()