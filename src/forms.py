from flask_wtf import Form
from wtforms import StringField, PasswordField, DateTimeField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

from datetime import datetime

from models import User

def username_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError("User with that name exists")


class UserRegistration(Form):
    username = StringField(
                'username',
                validators=[DataRequired(), username_exists]
    )
    password = PasswordField(
                'password',
                validators=[DataRequired(), Length(min=5)]
    )
    password2 = PasswordField(
                'Confirm password',
                validators=[DataRequired(), EqualTo('password', "Passwords must match")]
    )

class LoginForm(Form):
    username = StringField(
                'username',
                validators=[DataRequired()]
    )

    password = PasswordField(
                'password',
                validators=[DataRequired()]
    )

class checkInForm(Form):
    timeIn = DateTimeField(
            'timeIn',
            validators=[DataRequired()]
    )
