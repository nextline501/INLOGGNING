from flask import request
from queries import getUserbasedOnEmail
from flask_jwt_extended import create_access_token
from database import storeLoginData
import bcrypt

##Login logic 
def loginLogic(data):
    print("from login logic")
    print(data.get('email', None))

    ##data is passed in
    email = data.get('email', None)
    password = data.get('password', None)

    ##we check if the data is valid
    if not email: 
        return 'Missing email', 400
    if not password:
        return 'Missing password', 400
    
    ##we get user based on email
    user = getUserbasedOnEmail(email)
    if not user:
        return 'User Not Found!', 404

    ##we decrypt the encrypted password from the data base and see if the password is a match
    #if the password match we create an access_token that will be used to access the secrete api.. @app.route('/api/secreteData)
    if bcrypt.checkpw(password.encode('utf-8'), user['password']):
        ##now we can store login data since we know it's the correct password
        storeLoginData(data)
        ##access_token is created when password is confirmed
        access_token = create_access_token(identity=email)

        return {"access_token": access_token}, 200
    else:
        return 'Wrong Password'