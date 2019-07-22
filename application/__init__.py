# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy and Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig, ProductionConfig

# Import the flask-login authentication module
from flask_login import LoginManager, login_required


# Initialize pymysql for mysql support in deployment
import pymysql
pymysql.install_as_MySQLdb()

# Import the reverse proxy fix library
from flask_reverse_proxy_fix.middleware import ReverseProxyPrefixFix


import os

# Initialize the database instance for storing all the information
db = SQLAlchemy()

# Initialize the database migrate instance
migrate = Migrate()

# Initialize the login instance
login_manager = LoginManager()
"""
 Encapsulate the app in a function in order to be able to initialize it with
 various environment variables for  testing as well as versatility
"""
def create_app():
    # Define the application object


    # Change to production configuration if in production
    if(os.environ['ENVIRONMENT'] == 'PRODUCTION'):
        flask_app = Flask(__name__, static_url_path = '/makeuoft/static')
        #flask_app = Flask(__name__)
        config_class=ProductionConfig()
        from flask_reverse_proxy_fix.middleware import ReverseProxyPrefixFix
        ReverseProxyPrefixFix(flask_app)


    else:
        flask_app = Flask(__name__)
        config_class=DevelopmentConfig()



    # Configurations taken from function argument
    flask_app.config.from_object(config_class)

    # Initialize the various models with the flask_app
    db.init_app(flask_app)
    migrate.init_app(flask_app, db)

    # Create a LoginManager instance
    login_manager.init_app(flask_app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message= ''


    # Sample HTTP error handling
    @flask_app.errorhandler(404)
    def not_found(error):
        return render_template("404.html"), 404


    # Import a module / component using its blueprint handler variable (mod_auth)
    #from application.mod_auth.controllers import mod_auth as auth_module
    from application.home import home as home_module
    from application.auth import auth as auth_module

    # Register blueprint(s) - connects each module to the main flask application
    # app.register_blueprint(xyz_module)

    flask_app.register_blueprint(home_module)
    flask_app.register_blueprint(auth_module)


    return flask_app

from application import db_models

# Import the custom Command Line Interface file for custom flask commands
from application import cli
