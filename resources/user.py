import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel


class userRegister(Resource):
    parser=reqparse.RequestParser()

    parser.add_argument("username",
    type=str,
    required=True,
    help="please enter the valid name",
    )

    parser.add_argument("password",
    type=str,
    required=True,
    help="please enter the valid password",
    )

    def post(self):
        data=userRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return {"message":"User with this name already exist in our database"}

        else:
            user=UserModel(data['username'],data['password'])
            user.save_to_db()
            return {"message":"User has been created successfully"}

