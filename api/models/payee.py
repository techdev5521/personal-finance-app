"""Payee Model and Schema"""
import uuid as uuid_lib
from .models import db, ma
from .guid import GUID
from .category import Category


class Payee(db.Model):
    """Payee Model for SQLAlchemy"""

    __tablename__ = 'payee'
    id = db.Column(db.Integer, primary_key=True)
    fk_last_category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    uuid = db.Column(GUID, nullable=False, default=str(uuid_lib.uuid4()), unique=True, index=True)
    name = db.Column(db.String(255), nullable=False)

    category = db.relationship('Category', backref=db.backref('payees'))


class PayeeSchema(ma.SQLAlchemyAutoSchema):
    """Payee Schema for Marshmallow"""

    class Meta:
        """Schema Options"""
        model = Payee
        include_fk = True
