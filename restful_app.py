from flask import Flask,request
from flask_restful import Resource,Api
from flask_jwt import JWT,jwt_required
from security import authenticate, identity
from flask_sqlalchemy import SQLAlchemy

from resources.user import UserRegister
from resources.item import Item,ItemList
from models.item import ItemModel
from models.user import User
from db import db




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/dev/Documents/karthika/app/duplicate/code_section6/code/dbdata.db'
app.config['PROPAGATE_EXCEPTIONS'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = 'jose'
db.init_app(app)
db = SQLAlchemy(app)
api = Api(app)

    
@app.before_first_request
def create_table():
    db.create_all()


jwt = JWT(app,authenticate,identity)




api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')

if __name__ == '__main__':
    # db.create_all()
    db.init_app(app)
    app.run(port = 5001, debug=True)