from flask_restful import Resource,reqparse
from flask_jwt import JWT,jwt_required
from models.item import ItemModel

import sqlite3

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type = str,
    required = True,
    help = 'this field is important'
    )
    
    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'item not found'}
        
    

   
    def post(self,name):
        
        if ItemModel.find_by_name(name):
            return {'message':'item with this name already exists'},400

        data = Item.parser.parse_args()
        item = ItemModel(name,data['price'])
        try:
            #item.insert()
            item.save_to_db()
        except:
            return {'message':'an error occured inserting item'},500

        

        return item.json(),201

    

    def delete(self,name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "delete from users where name = ?"
        # cursor.execute(query,(name,))
        # connection.commit()
        # connection.close()

        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()


    # def put(self,name):
    #     data = Item.parser.parse_args()
    #     item = ItemModel.find_by_name(name)
    #     updated_item = ItemModel(name,data['price'])
    #     if item is None:
    #         try:
    #             updated_item.insert()
    #         except:
    #             return {'message':'an error occured inserting item '},500
    #     else:
    #         try:
    #             updated_item.update()
    #         except:
    #             return {'message':'an error occured updating item'},500

    #     return updated_item.json()

    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name,data['price'])
        else:
            item.price = data['price']

        item.save_to_db()
        return item.json()

   

class ItemList(Resource):
    def get(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "select * from items"
        # result = cursor.execute(query)
        # items = []

        # for row in result:
        #     items.append({"name":row[0],"price":row[1]})

        # connection.commit()
        # connection.close()
        # return {'items':items}
        return {'item':[item.json() for item in ItemModel.query.all()]}