from flask_wtf import FlaskForm
from flask_login import current_user
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
    EqualTo,
    ValidationError
)
from flaskblog.models import User



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
    submit = SubmitField('Sign Up')
    
    # creating a custom valiation
    def validate_username(self, username):
        # checking if the user credentials is already in our db then we get the first user else we get none and the new user signin successfully
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is taken. Please choose a different one.')
    
    # creating a custom valiations
    def validate_email(self, email):
        # checking if the user credentials is already in our db then we get the first user else we get none and the new user signin successfully
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is taken. Please choose a different one.')
    
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




class UpdateAccountForm(FlaskForm):
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
    submit = SubmitField('Update')
    
    # creating a custom valiation
    def validate_username(self, username):
        # checking if the user credentials is already in our db then we get the first user else we get none and the new user signin successfully
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username is taken. Please choose a different one.')
    
    # creating a custom valiations
    def validate_email(self, email):
        if email.data != current_user.email:
        # checking if the user credentials is already in our db then we get the first user else we get none and the new user signin successfully
            user = User.query.filter_by(email=email.data).first()
            if user: 
                raise ValidationError('This email is taken. Please choose a different one.')
