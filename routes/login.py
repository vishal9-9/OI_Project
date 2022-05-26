from flask import Blueprint, request
from database import models,database
from routes import tokens
from routes import passhash

login = Blueprint('login',__name__)

db = database.db

@login.route('/login',methods = ['GET','POST'])
def auth():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        check_user = db.query(models.Users).filter( models.Users.email == email ).first()
        if check_user:
            if  passhash.unhash(check_user.password,password):
                access_token =  tokens.create_token({'sub': check_user.email})
                return {"access_token": access_token, "token_type": "bearer"}
            else:
                return 'Wrong Credentials',401
        else:
            return 'User Not Found',401
    return 'Please Login',201

@login.route('/home', methods = ['GET'])
def home():
    return 'User Logged In',201