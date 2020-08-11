from .example import Example
from .user import UserRoute
from flask_restful import Api

def init_app(app):
    """Initializes flask-restful routes and endpoints

    Args:
        app (Flask): The flask app context
    """
    api = Api(app)
    api.add_resource(UserRoute, '/api/user')