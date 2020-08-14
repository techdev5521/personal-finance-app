"""Category Schema and Model"""
import uuid as uuid_lib
from .models import db, ma
from .guid import GUID


class CategoryModel(db.Model):
    """Category Model for SQLAlchemy"""

    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(GUID, nullable=False, default=str(uuid_lib.uuid4()), unique=True, index=True)
    name = db.Column(db.String(255), nullable=False)


class CategorySchema(ma.SQLAlchemyAutoSchema):
    """Category Schema for Marshmallow"""

    class Meta:
        """ Schema Options"""
        model = CategoryModel
        include_fk = True
        exclude = ('id',)
