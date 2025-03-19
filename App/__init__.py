from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'fb74ce263b68c0366834ea5a'

#Initialize Extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#Initialize LoginManager
login_manager = LoginManager(app)
login_manager.login_view = "login_page" #
login_manager.login_message_category = "info"
migrate = Migrate(app,db)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Port for sending email
app.config['MAIL_USERNAME'] = 'bharataggarwal2k2@gmail.com'  # Your email address
app.config['MAIL_PASSWORD'] = 'yihuonisfszfvpqm'    # os.environ.get("Email_Password")  Your email password
app.config['MAIL_USE_TLS'] = True  # Use TLS for secure connection
app.config['MAIL_USE_SSL'] = False  # Use SSL (only if required)

mail = Mail(app)

app.app_context().push()

from App import routes
