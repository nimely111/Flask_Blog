from flask_wtf import FlaskForm
# import form fields
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField
)
# import validations for form fields
from wtforms.validators import (
    DataRequired, 
    Length, 
    Email, 
    EqualTo
)


class RegistrationForm(FlaskForm):
    username = StringField(
                    'Username', 
                    validators=[DataRequired(), 
                    Length(min=2, max=20)]
                    )
    email = StringField(
                    'Email',
                    validators=[DataRequired(), 
                                Email()]
                    )
    password = PasswordField(
                    'Password', 
                    validators=[DataRequired()]
                    )
    confirm_password = PasswordField(
                    'Confirm Password', 
                    validators=[DataRequired(), 
                    EqualTo('password')]
                    )
    submit = SubmitField(
                    'Sign Up'
                    )
    
# Login form
class LoginForm(FlaskForm):
    email = StringField(
                    'Email',
                    validators=[DataRequired(), 
                    Email()]
                    )
    password = PasswordField(
                    'Password', 
                    validators=[DataRequired()]
                    )
    remember = BooleanField(
                    'Remember Me'
                    )
    submit = SubmitField('Login')
    