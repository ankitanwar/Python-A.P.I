from flask_restful import Resource,reqparse
from models.store import StoreModel

class Store(Resource):

    def get(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {"message":"Store not found in the database"}
         
    def post(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            return {"message":"Store with this name already exist in the database"}
        else:
            store=StoreModel(name)
            try:
                store.save_to_db()
                return {"message":"store has been created successfully"}
            except Exception as e:
                return {"message":"some error has been occured{}".format(e)}
                
    def delete(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            StoreModel.delete_from_db(store)
            return {"message":"store has been deleted successfully"}    
        else:
            return {"message":"Store not found in the database"}


class Stores(Resource):
    def get(self):
        return {"store":[store.json() for store in StoreModel.query.all()]}