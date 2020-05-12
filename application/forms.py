from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length

class AdminLoginForm(FlaskForm):
    user_name = StringField('User Name',
        validators = [
            DataRequired(),
            Length(min=5, max=20)
        ]
    )
    email_address = StringField('Email Address',
        validators = [
            DataRequired(),
            Length(min=10, max=30)
        ]
    )
    password = PasswordField('Password',
        validators = [
            DataRequired(),
            Length(min=8, max=40)
        ]
    )

    login = SubmitField('Login')

