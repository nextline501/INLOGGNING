from flask import Flask
from flask import g

import sqlite3
import bcrypt

##database path
DATABASE = './userInfo.db'

##Connect db
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

    ## To simplify working with SQLite, a row factory function is useful. 
    ## It is executed for every result returned from the database to convert the result.
    def make_dicts(cursor, row):
        return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))
    
    db.row_factory = make_dicts
    return db

##query function
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


##Function that takes data from the endpoint and inserts the data in to the database
def saveUserProfileData(data):
    print(data)

    hashedPW = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    
    try:
        user_id = data['id']
        email = data['email']
        user_password = hashedPW
        created = data['created']
        lastTimeLoggedIn = data['lastLoggedIn']
        timesLoggedIn = data['timesLoggedIn']

        print(user_id, email, user_password, created, lastTimeLoggedIn, timesLoggedIn)

        with sqlite3.connect(DATABASE) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO users (id, email, password, created, lastTimeLoggedIn, timesLoggedIn) VALUES (?, ?, ?, ?, ?, ?)",(user_id, email, user_password, created, lastTimeLoggedIn, timesLoggedIn) )
            
            con.commit()
            msg = "Record successfully added"
    except:
        con.rollback()
        msg = "error in insert operation"
        print("something went wrong")
    finally:
        con.close()

def updatePasswordBasedOnEmail(newPassword, email):
    print(newPassword)

    ##Encrypt the new updated password
    hashedPW = bcrypt.hashpw(newPassword.encode('utf-8'), bcrypt.gensalt())
    
    try:
        user_password = hashedPW;

        with sqlite3.connect(DATABASE) as con:
            cur = con.cursor()
            cur.execute( 'UPDATE users SET password = ? WHERE email = ?', (user_password, email) )
            
            con.commit()
            msg = "Record successfully added"
    except:
        con.rollback()
        msg = "error in insert operation"
        print("something went wrong")
    finally:
        con.close()
    
def deleteAccountFromDB(email):
    try:
        user_email = email

        with sqlite3.connect(DATABASE) as con:
            cur = con.cursor()
            cur.execute( 'DELETE FROM users WHERE email = ?', (user_email) )
            
            con.commit()
            msg = "Record successfully added"
    except:
        con.rollback()
        msg = "error in insert operation"
        print("something went wrong")
    finally:
        con.close()