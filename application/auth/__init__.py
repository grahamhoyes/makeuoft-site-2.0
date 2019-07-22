from flask import Blueprint

# Create the admin Blueprint
auth = Blueprint('auth', __name__, url_prefix='/auth')


from application.auth import controllers
