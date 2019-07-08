from application import db
import datetime
from sqlalchemy import DateTime
from sqlalchemy.sql import func

class MailingList(db.Model):
    __tablename__ = 'MailingList'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), index=True, unique=True, nullable=False)

    def __repr__(self):
        return '<Email {}>'.format(self.id) #prints <Email 'id'>
