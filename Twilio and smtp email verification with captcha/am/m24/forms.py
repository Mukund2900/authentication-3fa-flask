from flask_wtf import FlaskForm , RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField , TextAreaField , SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo , ValidationError
from m24.models import User , Personal , Security_ques

class RegistrationForm(FlaskForm):
    recaptch  = RecaptchaField()
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    mobile = StringField('mobile',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    first_name = StringField('first name',validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('last name',validators=[DataRequired(), Length(min=2, max=20)])
    userid = StringField('Userid',validators=[DataRequired(), Length(min=2, max=20)])
    ssnid = StringField('Enter the id', validators=[DataRequired(), Length(min=2, max=20)] )
    ssn_type = SelectField('Select the Government-id ',choices=[('Voter ID', 'Voter ID'), ('PAN Card' , 'PAN Card'), ('Aadhaar Card' , 'Aadhaar Card'), ('Driver License' , 'Driver License')])
    ques1 = SelectField('ques1',choices=[('Mothers Maiden Name ?', 'Mothers Maiden Name ?'), ('Pets Name ?' , 'Pets Name ?'), ('First Teachers Name ?' , 'First Teachers Name ?'), ('Favourite Holiday Destination?' , 'Favourite Holiday Destination?')])
    ques2 = SelectField('ques2',choices=[('Your Childhood Hero?' ,'Your Childhood Hero?' ), ('Time Of The Day Were You Born ?' , 'Time Of The Day Were You Born ?'), ('The steet you grew up in?' , 'The steet you grew up in?'), ('Your Childhood Nickname?' , 'Your Childhood Nickname?')])
    ans1 = StringField('ans1', validators=[DataRequired(), Length(min=2, max=20)] )
    ans2 = StringField('ans2', validators=[DataRequired(), Length(min=2, max=20)] )

    #dob = DateField('date of birth' , validators=DataRequired() , format = '%d/%m/%y' )
    submit = SubmitField('Done')
    def validate_userid(self, userid):
        personal = Personal.query.filter_by(userid=userid.data).first()
        if personal:
            raise ValidationError('That userid is taken. Please choose a different one.')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')
    def validate_password(self, field):
        uCase = 0
        _suggest = "\n"
        lCase = 0
        num = 0
        splChar = 0
        lent = 0
        flag = 0
        VAL = field.data
        if len(VAL)<8 or len(VAL)>16:
            lent = 0
        else:
            lent = 1
        for i in range (0,len(VAL)):
           if VAL[i].isupper():
               uCase = 1
           if VAL[i].islower():
               lCase = 1
           if VAL[i].isdigit():
               num = 1
           if (not(VAL[i].isupper()) and not(VAL[i].islower()) and not(VAL[i].isdigit())):
                   splChar = 1

        if not(uCase):
            raise ValidationError('Must Have One Upper Case Char.\n')
        else :
            _suggest = _suggest + ""
        if not(lCase):
            raise ValidationError('Must Have One Lower Case Char.\n')
        if not(num):
            raise ValidationError('Must Have One Digit.\n')
            flag += 1
        if not(splChar):
            raise ValidationError('Must Have One Special Char.\n ' )
        if not(lent):
            raise ValidationError('Must Be Between 8 and 16 characters long')
            flag += 1
        if(not(len(VAL))):
            flag +=1
            _suggest =  "\n"

class LoginForm(FlaskForm):
    recaptch  = RecaptchaField()
    email = StringField('Email',validators=[DataRequired(), Email()])
    mobile = StringField('Mobile',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    otp  = StringField('Enter the otp',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    ques1 = SelectField('ques1',choices=[('Mothers Maiden Name ?', 'Mothers Maiden Name ?'), ('Pets Name ?' , 'Pets Name ?'), ('First Teachers Name ?' , 'First Teachers Name ?'), ('Favourite Holiday Destination?' , 'Favourite Holiday Destination?')])
    ques2 = SelectField('ques2',choices=[('Your Childhood Hero?' ,'Your Childhood Hero?' ), ('Time Of The Day Were You Born ?' , 'Time Of The Day Were You Born ?'), ('The steet you grew up in?' , 'The steet you grew up in?'), ('Your Childhood Nickname?' , 'Your Childhood Nickname?')])
    ans1 = StringField('ans1', validators=[DataRequired(), Length(min=2, max=20)] )
    ans2 = StringField('ans2', validators=[DataRequired(), Length(min=2, max=20)] )


class GameForm(FlaskForm):
    content = StringField('OTP' , validators=[DataRequired()])
    submit = SubmitField('verify')



class FstepForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    mobile = StringField('Mobile',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Send')

