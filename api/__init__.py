from flask import Flask

# Initialize the whole api
def create_app():
    from . import models, routes

    # App instance creation
    app = Flask(__name__)

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../personal_finance-dev.db'

    # Submodule Initialization
    models.init_app(app)
    routes.init_app(app)
    return app