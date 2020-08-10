from .models import db, ma
from .guid import GUID

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(GUID, nullable=False)
    name = db.Column(db.String(255), nullable=False)

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        include_fk = True