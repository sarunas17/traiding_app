from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField, PasswordField, FloatField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email
from flask_wtf.file import FileField, FileAllowed
from main import User, current_user


class RegistracionForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    password_confirmed = PasswordField("Confirm your password", [EqualTo('password', "Password and confirm password should be the same.")])
    submit = SubmitField('Register')


    def check_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This e-mail email address is used. Choose another.')


class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField('Log in') 