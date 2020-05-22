from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, FloatField, IntegerField
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

class AddShoeForm(FlaskForm):
    shoe_id = StringField('Shoe ID',
        validators=[
            DataRequired(),
            Length(max=3)
        ])
    shoe_name = StringField('Shoe Name',
        validators=[
            DataRequired()
        ])
    shoe_size = StringField('Shoe Size',
        validators=[
            DataRequired(),
            Length(max=2)
        ])
    shoe_price = FloatField('Shoe Price',
        validators=[
            DataRequired()
        ])
    submit = SubmitField('Add')

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

class UpdateQuantityForm(FlaskForm):
    quantity = IntegerField('Quantity',
        validators=[
            DataRequired(),
            Length(max=100)
        ])
    submit = SubmitField('Update')