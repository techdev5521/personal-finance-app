from .db_models import db

# Initialize sqlalchemy db backend
def init_app(app):
    db.init_app(app)