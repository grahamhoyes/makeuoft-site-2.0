from application import db
import datetime
from sqlalchemy import DateTime
from sqlalchemy.sql import func

# Import class to provide functions for login of admins
from flask_login import UserMixin
from application import login_manager

# Import class to create and check password hashes
from werkzeug.security import generate_password_hash, check_password_hash

class MailingList(db.Model):
    __tablename__ = 'MailingList'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), index=True, unique=True, nullable=False)

    def __repr__(self):
        return '<Email {}>'.format(self.id) #prints <Email 'id'>


class Users(UserMixin, db.Model):
    # Define the columns of the table, including primary keys, unique, and
    # indexed fields, which makes searching faster
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), index=True, nullable=False)
    last_name = db.Column(db.String(255), index=True, nullable=False)
    email = db.Column(db.String(255), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_date = db.Column(DateTime(), server_default=func.now()) #func.now() tells the db to calculate the timestamp itself rather than letting the application do it
    updated_date = db.Column(DateTime(), onupdate=func.now())

    # __repr__ method describes how objects of this class are printed
    # (useful for debugging)
    def __repr__(self):
        return '<User {}>'.format(self.id) #prints <User 'id'>

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
