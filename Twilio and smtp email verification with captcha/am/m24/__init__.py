from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LeGVQEVAAAAAMYCwSxdCHOkxFM0f2Tbf0oQJVUh'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LeGVQEVAAAAABw6fcAxZs3nBDybsBZws-b_4b5m'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'Kemparty9@gmail.com'
app.config['MAIL_PASSWORD'] = 'cheatcodes123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
account_sid = 'AC02169fc075008d1b476d199e0e835cd5'
auth_token = '2de1db15ee70385356ffdd16618d6de9'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
from m24 import routes