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

from database import get_db, query_db, saveUserProfileData
from queries import getAllUsers, getUserbasedOnEmail

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
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email: 
        return 'Missing email', 400
    if not password:
        return 'Missing password', 400
    
    user = getUserbasedOnEmail(email)
    if not user:
        return 'User Not Found!', 404
    
    print('222222222222222')
    print(password)
    print(user['password'])
    print(user)
    print('222222222222222')

    if bcrypt.checkpw(password.encode('utf-8'), user['password']):
        access_token = create_access_token(identity={email: email, password: password})
        return {"access_token": access_token}, 200
    else:
        return 'Wrong Password'

    return 'Post ok'

@app.route('/api/secreteData', methods = ['GET'])
#When jwt is added we have secured the route
@jwt_required
def identity():
    user = get_jwt_identity
    print(user)
    return 'Secrete data', 200

##close_connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

