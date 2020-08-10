from .models import db, ma
from .guid import GUID
from .category import Category

class Payee(db.Model):
    __tablename__ = 'payee'
    id = db.Column(db.Integer, primary_key=True)
    fk_last_category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    uuid = db.Column(GUID, nullable=False)
    name = db.Column(db.String(255), nullable=False)

    category = db.relationship('Category', backref=db.backref('payees'))

class PayeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Payee
        include_fk = True