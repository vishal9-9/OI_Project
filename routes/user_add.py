from flask import Blueprint
from routes import check_role

user_add = Blueprint('user_add',__name__)

@user_add.route('/user_add', methods = ['GET'])
def add_user():
    a = check_role.check_role(1)
    return a