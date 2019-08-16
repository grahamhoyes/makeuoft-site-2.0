from flask import render_template
#from application import flask_app
#from application.db_models import Users, Teams, PartsAvailable, PartsSignedOut, Tag, tags
from application import db # import the db instance from application/__init__.py
from flask import jsonify
import click
import os
import json

# Import mail
from application import mail
from flask_mail import Message

"""
Encapsulate the commands in a function to be able to register it with the application
and pass different parameters if the need arises
"""
def register(flask_app):
    @flask_app.cli.group()
    def test():
        """Testing commands for various services"""
        pass
    @test.command()
    def mailsend():
        """Sends a test email through the makeuoft email account"""
        #    msg = Message('Confirm Email', sender= 'email@address.com', recipients= [session['email']])
        msg = Message('Test', recipients= ['some_email@example.com'])
        msg.body = 'This is a test'
        msg.html = render_template('mails/reset-password.html', username="Test Subject", link="github.com")
        mail.send(msg)
