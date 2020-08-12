import enum
import uuid as uuid_lib
from .models import db, ma
from .guid import GUID
from .account import Account
from .payee import Payee
from .category import Category

class TransactionType(enum.Enum):
    DEPOSIT = 1
    WITHDRAWAL = 2
    TRANSFER = 3
    
class Transaction(db.Model):
    """Transaction Model for SQLAlchemy

    Args:
        db (Model): Returns an SQLAlchemy Transaction object
    """
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    fk_withdrawal_account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    fk_deposit_account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    fk_payee_id = db.Column(db.Integer, db.ForeignKey('payee.id'), nullable=True)
    fk_category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    uuid = db.Column(GUID, nullable=False, default=str(uuid_lib.uuid4()), unique=True, index=True)
    date = db.Column(db.Date, nullable=False)
    type = db.Column(db.Enum(TransactionType), nullable=False)
    amount = db.Column(db.DECIMAL(14,2), nullable=False)
    check_number = db.Column(db.Integer, nullable=True)
    note = db.Column(db.String(255), nullable=True)

    withdrawal_account = db.relationship('Account', backref=db.backref('withdrawal_transactions'), foreign_keys=[fk_withdrawal_account_id])
    deposit_account = db.relationship('Account', backref=db.backref('deposit_transactions'), foreign_keys=[fk_deposit_account_id])
    payee = db.relationship('Payee', backref=db.backref('transactions'))
    category = db.relationship('Category', backref=db.backref('transactions'))

class TransactionSchema(ma.SQLAlchemyAutoSchema):
    """Transaction Schema for Marshmallow

    Args:
        ma (SQLAlchemyAutoSchema): Returns a Marshmallow Transaction Schema object for serialization/deserialization
    """
    class Meta:
        model = Transaction
        include_fk = True
