from database import query_db, get_db

def getAllUsers():
    for user in query_db('select * from users'):
        print(user['email'], 'has the id', user['id'])


def getUserbasedOnEmail(email):
    print('look here')
    print(email)

    user = query_db('select * from users where email = ?', [email], one=True)
    if user is None:
        print('No such user')
    else:
        print(user['email'], 'has the id', user['id'])
    return user
