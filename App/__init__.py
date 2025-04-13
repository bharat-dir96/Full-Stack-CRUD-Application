import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail

# load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

#Initialize Extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#Initialize LoginManager
login_manager = LoginManager(app)
login_manager.login_view = "login_page" #
login_manager.login_message_category = "info"
migrate = Migrate(app,db)


app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT'))  # Port for sending email
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # Your email address
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')    # os.environ.get("Email_Password")  Your email password
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS')  # Use TLS for secure connection
app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL')  # Use SSL (only if required)

mail = Mail(app)

app.app_context().push()

from App import routes
