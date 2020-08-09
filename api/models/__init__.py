from .db_models import db

# Initialize sqlalchemy db backend
def init_app(app):
    db.init_app(app)
    # TODO: Create setup script? of some sort and move database creation there
    with app.app_context():
        db.create_all()