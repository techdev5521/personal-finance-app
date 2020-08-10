import enum
from .models import db, ma
from .guid import GUID
from .user import User

# TODO: Not sure if the enum is done correctly
class AccountType(enum.Enum):
    CASH = 1
    BANK = 2
    CARD = 3

class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    fk_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    uuid = db.Column(GUID, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    type = db.Column(db.Enum(AccountType), nullable=False)
    bank = db.Column(db.String(255), nullable=True)
    bank_website = db.Column(db.String(255), nullable=True)
    account_number = db.Column(db.Integer, nullable=True)
    routing_number = db.Column(db.Integer, nullable=True)

    # Relationships
    user = db.relationship('User', backref=db.backref('accounts'))

class AccountSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Account
        include_fk = True