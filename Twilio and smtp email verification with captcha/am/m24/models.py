from datetime import datetime
from m24 import db , login_manager

from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    userid = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile = db.Column(db.Integer())
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    contactVerified = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(50), unique=True, nullable=False)
    last_name = db.Column(db.String(50), unique=True, nullable=False)    #dob = db.Column(db.datetime())
    ssn_type = db.Column(db.String(50))
    ssnid = db.Column(db.String(50))
    ques1 = db.Column(db.String(50))
    ques2 = db.Column(db.String(50))
    ans1 = db.Column(db.String(50))
    ans2 = db.Column(db.String(50))
    def __repr__(self):
        return f"User('{self.username}', '{self.userid}', '{self.email}', '{self.image_file}', '{self.mobile}', '{self.contactVerified}' ,  '{self.first_name}', '{self.last_name}', '{self.ssn_type}', '{self.ssnid}' , '{self.ques1 }' , '{self.ques2}', '{self.ans1}', '{self.ans2}')"


class Personal(db.Model):
    first_name = db.Column(db.String(50), unique=True, nullable=False)
    last_name = db.Column(db.String(50), unique=True, nullable=False)
    userid = db.Column(db.String(50), unique=True, nullable=False ,primary_key=True)
    #dob = db.Column(db.datetime())
    ssn_type = db.Column(db.String(50))
    ssnid = db.Column(db.String(50))
    def __repr__(self):
        return f"Personal( '{self.userid}' , '{self.first_name}', '{self.last_name}', '{self.ssn_type}', '{self.ssnid}')"

class Security_ques(db.Model):

    userid = db.Column(db.String(50), unique=True, nullable=False ,primary_key=True)
    ques1 = db.Column(db.String(50))
    ques2 = db.Column(db.String(50))
    ans1 = db.Column(db.String(50))
    ans2 = db.Column(db.String(50))
    def __repr__(self):
        return f"Security_ques( '{self.ques1 }' , '{self.ques2}', '{self.ans1}', '{self.ans2}')"



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), default=datetime.utcnow)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer,default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.title}','{self.content}', '{self.date_posted}')"
