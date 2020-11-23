from flask import  render_template,url_for,flash , redirect , request 
from m24 import app , db , bcrypt
from m24.forms import RegistrationForm,  LoginForm , GameForm ,FstepForm
from m24.models import User  , Personal ,Security_ques , Post
from flask_login import login_user, current_user , logout_user , login_required
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import socket
import twilio 
import random
from twilio.rest import Client
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'Kemparty9@gmail.com'
app.config['MAIL_PASSWORD'] = 'cheatcodes123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
account_sid = 'AC02169fc075008d1b476d199e0e835cd5'
auth_token = '2de1db15ee70385356ffdd16618d6de9'
otp = random.randint(1000 , 9999)
mail = Mail(app)
s = URLSafeTimedSerializer('Thisisasecret!')
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/play")
def play():
    return render_template('play.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(ques1 = form.ques1.data , ques2 = form.ques2.data , ans1 = form.ans1.data , ans2 = form.ans2.data , username=form.username.data,mobile = form.mobile.data ,  email=form.email.data, password=hashed_password , first_name=form.first_name.data ,last_name=form.last_name.data ,userid=form.userid.data , ssn_type=form.ssn_type.data, ssnid=form.ssnid.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('fstep'))
    return render_template('register.html', title='Register', form=form)




@app.route("/details", methods=['GET', 'POST'])
def details():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        personal = Personal(first_name=form.first_name.data ,last_name=form.last_name.data ,userid=form.userid.data , ssn_type=form.ssn_type.data, ssnid=form.ssnid.data)
        db.session.add(personal)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('details'))
    return render_template('register.html', title='Register', form=form)


@app.route("/fstep", methods=['GET', 'POST'])
def fstep():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = FstepForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user :
            email = request.form['email']
            mobile = request.form['mobile']    

            client = Client(account_sid, auth_token)
            tab = 1452
            print(otp)
            token = s.dumps(email, salt='email-confirm')
            msg = Message('Confirm Email', sender='Kemparty9@gmail.com', recipients=[email])
            message = client.messages.create(
                                              body='your otp is - '+str(otp),
                                              from_='+1 205 784 0664',
                                              to='+91'+str(mobile)
                                          )
            msg.body = 'your otp is - '+str(otp)
            mail.send(msg)
            return redirect(url_for('login'))
            return tab
        else:
            flash('verification Unsuccessful. Please check email and mobile', 'danger')
    return render_template('fstep.html', title='Fstep', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            if(int(form.otp.data) == otp) : 
                login_user(user, remember=form.remember.data)
                return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/game", methods=['GET', 'POST'])
@login_required
def game():
    form = GameForm()
    if form.validate_on_submit():
        post = Post(content = form.content.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('game.html', title='Register', form=form)



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))



@app.route("/account")
@login_required
def account():
    return render_template('account.html')


