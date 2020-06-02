import os
from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_admin import Admin

app=Flask(__name__)
app.config['SECRET_KEY']='81772acbcd46416113b290c870dfd1d5'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///base.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
now=datetime.now()
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'
app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']= 'nkakaeric96@gmail.com'
app.config['MAIL_PASSWORD']= 'isheja1994'
mail=Mail(app)
admin=Admin(app,name='Control Panel')

from flaskblog import routes