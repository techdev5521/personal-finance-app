from .models import db, ma
# Import all the models
from .user import *
from .account import *
from .category import *
from .payee import *
from .transaction import *

# Initialize sqlalchemy db backend
def init_app(app):
    db.init_app(app)
    ma.init_app(app)
    # TODO: Create setup script? of some sort and move database creation there
    with app.app_context():
        db.create_all()