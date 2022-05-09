from flask import Blueprint

auth = Blueprint('auth', __name__)

#Login page
@auth.route('/login/')
def loginpage():
    return "<h1>This is Login page!</h1>"