import enum
from flask_sqlalchemy import SQLAlchemy

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application
db = SQLAlchemy()

class User(db.Model):
    __tablename__= 'user'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.CHAR(16), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)

    # Relationships
    accounts = db.relationship('Account', backref=db.backref('user'))

# TODO: Not sure if the enum is done correctly
class AccountType(enum.Enum):
    CASH = 1
    BANK = 2
    CARD = 3

class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    fk_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    uuid = db.Column(db.CHAR(16), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    type = db.Column(db.Enum(AccountType), nullable=False)
    bank = db.Column(db.String(255), nullable=True)
    bank_website = db.Column(db.String(255), nullable=True)
    account_number = db.Column(db.Integer, nullable=True)
    routing_number = db.Column(db.Integer, nullable=True)

    # Relationships
    transactions = db.relationship('Transaction', backref=db.backref('account'))

class Payee(db.Model):
    __tablename__ = 'payee'
    id = db.Column(db.Integer, primary_key=True)
    fk_last_category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    uuid = db.Column(db.CHAR(16), nullable=False)
    name = db.Column(db.String(255), nullable=False)

    # Relationships
    transactions = db.relationship('Transaction', backref=db.backref('payee'))

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.CHAR(16), nullable=False)
    name = db.Column(db.String(255), nullable=False)

    # Relationships
    transactions = db.relationship('Transaction', backref=db.backref('category'))
    payees = db.relationship('Payee', backref=db.backref('category'))

class TransactionType(enum.Enum):
    DEPOSIT = 1
    WITHDRAWAL = 2
    TRANSFER = 3
    
class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    fk_withdrawal_account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    fk_deposit_account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    fk_payee_id = db.Column(db.Integer, db.ForeignKey('payee.id'), nullable=True)
    fk_category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    uuid = db.Column(db.CHAR(16), nullable=False)
    date = db.Column(db.Date, nullable=False)
    type = db.Column(db.Enum(TransactionType), nullable=False)
    amount = db.Column(db.DECIMAL(14,2), nullable=False)
    check_number = db.Column(db.Integer, nullable=True)
    note = db.Column(db.String(255), nullable=True)
