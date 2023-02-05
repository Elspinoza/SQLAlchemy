from app import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app.config['SECRET_KEY'] = "asus"

#===============================================Les routes pour la connexion avec la base de données =================================================================

#app.config['MYSQL_DATABASE_USER']= "root"
#app.config['MYSQL_DATABASE_HOST']= "localhost"
#app.config['MYSQL_DATABASE_PASSWORD']= ""

# =========================================================================

#app.config['MYSQL_DATABASE_DB']= "flask_sqlalchemy"


#==========================================================Connexion de la base de donnee SQLAlchemy===================================================================
# %s pour passer en parametre les parametres
# username, password, host
#app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://%s:%s@%s/%s"%('root', '', 'localhost', '3306', 'flask_sqlalchemy')
app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://root:Innocent2002@localhost/flask_sqlalchemy" #formatage
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#connexion a la base de donnee
db = SQLAlchemy(app)
#===========================================================================

#db.init_app(app)