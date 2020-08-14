"""Initializes FLask-RESTful Routes"""
from flask_restful import Api
from .example import ExampleRoute
from .login import LoginRoute
from .user import UserRoute
from .category import CategoryRoute



def init_app(app):
    """Initializes flask-restful routes and endpoints

    Args:
        app (Flask): The flask app context
    """
    api = Api(app)
    api.add_resource(ExampleRoute, '/api/example')
    api.add_resource(LoginRoute, '/api/login')
    api.add_resource(
        UserRoute,
        '/api/user/create',
        '/api/user/<string:uuid>',
        '/api/user/update/<string:uuid>',
        '/api/user/delete/<string:uuid>'
    )
    api.add_resource(
        CategoryRoute,
        '/api/category',
        '/api/category/<string:uuid>'
    )
