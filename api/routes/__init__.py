from .example import Example
from flask_restful import Api

# Initialize flask-restful backend
def init_app(app):
    api = Api(app)
    api.add_resource(Example, '/api/<string:name>')