import sqlite3
from flask_restful import Resource,reqparse
from models.user import User


    
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type = str,
    required = True,
    help = 'this field is important'
    )
    parser.add_argument('password',
    type = str,
    required = True,
    help = 'this field is important'
    )
    
    
    def post(self):
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data['name']):
            return {'message':'The user with this name already exists'},400
        
        #user = User(data['name'],data['price'])
        user = User(**data)
        user.save_to_db()
        return {'message':'user created successfully'},201


    


    
     
    

