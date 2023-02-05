from config import db

#Class User

class User(db.Model):

    #Creation de la table User avec ses attributs

    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(100), nullable = False)
