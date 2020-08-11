from flask import Flask
from . import models, routes
from api.tokens import ta

# App instance creation
app = Flask(__name__)
# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../personal_finance-dev.db'

models.init_app(app)
routes.init_app(app)