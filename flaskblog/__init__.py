from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
import os

app = Flask(__name__)
#application configurations
app.config['SECRET_KEY'] = '8e4268d5e6fa9ba74a5ba9463d833c35'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# flaskblog instances
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view ='login' #telling the extension where the login_view is located
migrate = Migrate(app, db)

from flaskblog import routes