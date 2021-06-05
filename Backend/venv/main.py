from flask import Flask
from flask import request
from flask import g
from flask_cors import CORS
from flask import jsonify

##create access function to create access token
from flask_jwt_extended import create_access_token
##gives you give info inside the token
from flask_jwt_extended import get_jwt_identity
##Decorator you put on routs, to protect the route
from flask_jwt_extended import jwt_required
##Hold functions and callbacks
from flask_jwt_extended import JWTManager

import sqlite3
import bcrypt

from database import get_db, query_db, saveUserProfileData, updatePasswordBasedOnEmail, deleteAccountFromDB
from queries import getAllUsers, getUserbasedOnEmail
from login import loginLogic

app = Flask(__name__)
cors = CORS(app)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "3a2aa4e770f417b11ca3bd8cdac52f0d3a2aa4e770f417b11ca3bd8cdac52f0d3a2aa4e770f417b11ca3bd8cdac52f0d"
jwt = JWTManager(app)


@app.route("/api/createUser", methods=['POST'])
def saveUserData():
    if request.method == 'POST':
        data = request.json
        saveUserProfileData(data)
        return "post ok"

@app.route('/api/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        data = request.json
        return loginLogic(data)

##This is where the magic happens, here we send a get request back to Vue. 
# @jwt_required() locks down this api thus we need the access token in the access_token in the http request
@app.route('/api/secreteData', methods = ['GET'])
@jwt_required()
def identity():
    if request.method == 'GET':
        user = get_jwt_identity()
        print(user)
        return user, 200

@app.route('/api/passwordChange', methods = ['POST'])
def passwordChange():
    if request.method == 'POST':
        print(request.json)
        email = request.json.get('email', None)
        newPassword = request.json.get('password', None)
        updatePasswordBasedOnEmail(newPassword, email)

        return "Password is now updated"

@app.route('/api/deleteAccount', methods = ['POST'])
def deleteAccount():
    if request.method == 'POST':
        email = request.json.get('email1')
        print("2222222")
        print(email)
        deleteAccountFromDB(email)
        return "Account is now deleted"

##close_connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

