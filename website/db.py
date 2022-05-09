from flask import Blueprint,render_template, request
from flask_mysqldb import MySQL

db = Blueprint('db', __name__)

#Setting up MYSQL database
db.config['MYSQL_HOST'] = 'localhost'
db.config['MYSQL_USER'] = 'root'
db.config['MYSQL_PASSWORD'] = ''
db.config['MYSQL_DB'] = 'flask'

mysql = MySQL(db)
