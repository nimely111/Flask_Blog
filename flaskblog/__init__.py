from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
#application configurations
app.config['SECRET_KEY'] = '8e4268d5e6fa9ba74a5ba9463d833c35'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# flaskblog instances
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flaskblog import routes