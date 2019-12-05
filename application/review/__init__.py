from Flask import Blueprint

review = Blueprint('review', __name__, url_prefix='/review')

from application.home import controllers
