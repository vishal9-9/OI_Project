from sys import prefix
from flask import Flask
from database import models
from database import database
from routes import login,user_add

def create_app():
    app = Flask(__name__)
    app.register_blueprint(login.login,prefix='/')
    app.register_blueprint(user_add.user_add)
    models.Base.metadata.create_all(bind = database.engine)
    return app