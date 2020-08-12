from .example import ExampleRoute
from .user import UserRoute
from .login import LoginRoute
from flask_restful import Api

def init_app(app):
    """Initializes flask-restful routes and endpoints

    Args:
        app (Flask): The flask app context
    """
    api = Api(app)
    api.add_resource(ExampleRoute, '/api/example')
    api.add_resource(UserRoute, '/api/user')
    api.add_resource(LoginRoute, '/api/login')