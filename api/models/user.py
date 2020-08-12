import uuid as uuid_lib
from .models import db, ma
from .guid import GUID

class User(db.Model):
    """User Model for SQLAlchemy"""

    __tablename__= 'user'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(GUID, nullable=False, default=str(uuid_lib.uuid4()))
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

class UserSchema(ma.SQLAlchemyAutoSchema):
    """User Schema for Marshmallow"""
    
    class Meta:
        model = User
        include_fk = True