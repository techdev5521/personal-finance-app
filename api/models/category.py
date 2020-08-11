import uuid as uuid_lib
from .models import db, ma
from .guid import GUID

class Category(db.Model):
    """Category Model for SQLAlchemy

    Args:
        db (Model): Returns an SQLAlchemy Category object
    """
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(GUID, nullable=False, default=str(uuid_lib.uuid4()))
    name = db.Column(db.String(255), nullable=False)

class CategorySchema(ma.SQLAlchemyAutoSchema):
    """Category Schema for Marshmallow

    Args:
        ma (SQLAlchemyAutoSchema): Returns a Marshmallow Category Schema object for serialization/deserialization
    """
    class Meta:
        model = Category
        include_fk = True