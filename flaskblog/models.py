from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flaskblog import db,login_manager,app,admin
from flask_login import UserMixin,current_user
from  flask_admin.contrib.sqla import ModelView
from flask import abort

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model,UserMixin):
 id=db.Column(db.Integer,primary_key=True)
 username=db.Column(db.String(20),unique=True,nullable=False)
 email=db.Column(db.String(120),unique=True,nullable=False)
 image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
 password=db.Column(db.String(60),nullable=False)
 is_admin=db.Column(db.Boolean,default=False)
 posts=db.relationship('Post',backref='author',lazy=True)

 def get_reset_token(self,expires_sec=1800):
     s=Serializer(app.config['SECRET_KEY'],expires_sec)
     return s.dumps({'user_id':self.id}).decode('utf-8')

 @staticmethod
 def verify_reset_token(token):
    s=Serializer(app.config['SECRET_KEY'])
    try:
      user_id=s.loads(token)['user_id']

    except:
      return None
    return User.query.get(user_id)

 def __repr__(self):
     return f"User('{self.username}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
     return f"Post('{self.title}','{self.date_posted}')"

# class Controller(ModelView):
#   def is_accessible(self):
#     if current_user.is_admin==True:
#       return current_user.is_authenticated
#     else:
#       abort(404)
#   def not_auth(self):
#     return 'You are not allowed to use this page.'


# admin.add_view(Controller(User,db.session))
# admin.add_view(ModelView(Post,db.session))
