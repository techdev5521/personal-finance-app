"""User Model and Schema"""
import uuid as uuid_lib
from .models import db, ma
from .guid import GUID


class UserModel(db.Model):
    """User Model for SQLAlchemy"""

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(GUID, nullable=False, default=str(uuid_lib.uuid4()), unique=True, index=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(255), nullable=False, unique=True)


class UserSchema(ma.SQLAlchemyAutoSchema):
    """User Schema for Marshmallow"""

    class Meta:
        """Schema Options"""
        model = UserModel
        include_fk = True
        exclude = ('id', 'password_hash')
