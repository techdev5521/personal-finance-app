from .models import db, ma


class ExampleModel(db.Model):
    # """Example Model for SQLAlchemy"""

    __tablename__ = 'example'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

class ExampleSchema(ma.SQLAlchemyAutoSchema):
    """Example Schema for Marshmallow"""

    class Meta:
        model = ExampleModel
        include_fk = True
