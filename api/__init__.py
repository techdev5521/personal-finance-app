from flask import Flask
from . import models, routes
from api.security import ta, ph

# Create Flask App Instance
app = Flask(__name__)

# Configure SQLAlchmey to use SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../personal_finance-dev.db'

# Initialize SQLAlchemy and Marshmallow
models.init_app(app)

# Initialize Flask-RESTFul Models
routes.init_app(app)