from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users, Shoes
from flask_login import current_user

class LoginForm(FlaskForm):
    email = StringField('Email Address',
        validators = [
            DataRequired(),
            Email(),
            Length(max=50)
        ]
    )
    password = PasswordField('Password',
        validators = [
            DataRequired(),
        ]
    )

    remember = BooleanField('Remember Me?')
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    user_name = StringField('User Name',
         validators = [
             DataRequired(),
             Length(min=6, max=20)
        ]
    )
    email = StringField('Email Address',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password',
        validators = [
            DataRequired(),
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')
    
    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already assigned to a User!')

class UpdateShoeForm(FlaskForm):
    shoe_name = StringField('Shoe Name',
        validators=[
            DataRequired()
        ])
    shoe_price = FloatField('Shoe Price',
        validators=[
            DataRequired()
        ])
    submit = SubmitField('Update')

def shoe_query():
    return Shoes.query