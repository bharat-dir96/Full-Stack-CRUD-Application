from App import db, login_manager
from App import bcrypt
from flask_login import UserMixin
from datetime import datetime
import pytz

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))     #Fetch user by id

#Database for user personal details
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True, autoincrement = True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    full_name = db.Column(db.String(length=50), nullable=False)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    job_title = db.Column(db.String(length=100), nullable=False)
    hash_password = db.Column(db.String(length=60), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow().replace(tzinfo=pytz.UTC).astimezone(pytz.timezone('Asia/Kolkata')), nullable=False)
    last_login = db.Column(db.DateTime(), default=datetime.utcnow().replace(tzinfo=pytz.UTC).astimezone(pytz.timezone('Asia/Kolkata')), nullable=True)
    verification_token=db.Column(db.String(32), unique=True)
    is_verified = db.Column(db.Boolean, default=False)

    def get_id(self):
        return str(self.id)

    def update_last_login(self):
        self.last_login = datetime.utcnow().replace(tzinfo=pytz.UTC).astimezone(pytz.timezone('Asia/Kolkata'))
        db.session.commit()

    @property
    def password(self):
        raise AttributeError("Password is not readable!")


    @password.setter
    def password(self, plain_text_password):
        self.hash_password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.hash_password, attempted_password)


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement = True)
    post_title = db.Column(db.String(length=200), nullable=False)
    post_description = db.Column(db.String(length=2000),nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow().replace(tzinfo=pytz.UTC).astimezone(pytz.timezone('Asia/Kolkata')), nullable=False)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow().replace(tzinfo=pytz.UTC).astimezone(pytz.timezone('Asia/Kolkata')), nullable=False)
    
    
