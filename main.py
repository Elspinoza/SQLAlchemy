from app import app
from config import db
from model import User
from flask import request, jsonify
import json


#Creation de deux utilisateurs USER1 et USER2
# user1 = User(name = 'Ema')
# user2 = User(name = 'Inno')

app.app_context().push()
db.create_all()

#session.add ou .all execute la requete de creation
#db.session.all

# db.session.add(user1)
# db.session.add(user2)

# try:
#     db.session.commit()
# except Exception as e:
#     print(e)
#     db.session.rollback()
# finally:
#     db.session.close()

print(User.query.get('1'))

@app.route('/user/add', methods=['POST'])
def add_user():
    try:
        json = request.json
        print('==================================')
        print(json)
        print('==================================')
        name = json['name']
        if  name and request.method == 'POST':
            user = User(name = name)
            db.session.add(user)
            db.session.commit()
            resultat = jsonify('Utilsateur ajoute')
            #resultat.status_code = 200
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()
    
@app.route('/users', methods = ['GET'])
def get_all():
    try:
        users = User.query.all()
        data = [{"id":user.id,"name":user.name} for user in users]

        resultat = jsonify({"status_code": 200, "users" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()



if(__name__ == '__main__'):
    app.run()