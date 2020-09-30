from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity
from resources.user import userRegister
from resources.item import ItemList,Item
from resources.store import Store,Stores

app=Flask(__name__)
app.secret_key="secret key"    #should not be exposed to anyone should be long and complicated
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'   #location of the database
app.config["SQlALCHEMY_TRACK_MODIFICATION"]=False
app.config['PROPAGATE_EXCEPTIONS'] = True   
api=Api(app)

@app.before_first_request
def create_table():
    db.create_all()

jwt=JWT(app,authenticate,identity)

api.add_resource(Item,"/item/<string:name>")
api.add_resource(ItemList,"/items")
api.add_resource(userRegister,"/register")
api.add_resource(Store,"/store/<string:name>")
api.add_resource(Stores,"/stores")


if __name__=='__main__':
    from db import db
    db.init_app(app)   #init app ke andar app=Flask(__name__) wala app hai 
    app.run(debug=True)