# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy and Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig, ProductionConfig, PrefixMiddleware

# Initialize pymysql for mysql support in deployment
import pymysql
pymysql.install_as_MySQLdb()

import os

# Initialize the database instance for storing all the information
db = SQLAlchemy()

# Initialize the database migrate instance
migrate = Migrate()

# Initialize the login instance
"""
 Encapsulate the app in a function in order to be able to initialize it with
 various environment variables for  testing as well as versatility
"""
def create_app():
    # Define the application object
    flask_app = Flask(__name__)


    # Change to production configuration if in production
    if(os.environ['ENVIRONMENT'] == 'PRODUCTION'):
        config_class=ProductionConfig()
        flask_app.wsgi_app = PrefixMiddleware(flask_app.wsgi_app, prefix='makeuoft')

    else:
        config_class=DevelopmentConfig()





    # Configurations taken from function argument
    flask_app.config.from_object(config_class)

    # Initialize the various models with the flask_app
    db.init_app(flask_app)
    migrate.init_app(flask_app, db)

    # Sample HTTP error handling
    @flask_app.errorhandler(404)
    def not_found(error):
        return render_template("404.html"), 404


    # Import a module / component using its blueprint handler variable (mod_auth)
    #from application.mod_auth.controllers import mod_auth as auth_module
    from application.home import home as home_module

    # Register blueprint(s) - connects each module to the main flask application
    # app.register_blueprint(xyz_module)

    flask_app.register_blueprint(home_module)

    return flask_app

from application import db_models

# Import the custom Command Line Interface file for custom flask commands
from application import cli
