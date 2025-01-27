import sqlite3
from db import db
class UserModel(db.Model):

    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20))
    password=db.Column(db.String(20))  
    
    def __init__(self,username,password):
        self.username=username
        self.password=password

    @classmethod
    def find_by_username(cls,name):
        return UserModel.query.filter_by(username=name).first()

    @classmethod
    def find_by_id(cls,_id):
        return UserModel.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()