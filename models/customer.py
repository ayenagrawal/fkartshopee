from datetime import datetime
from fkart.models.base import BaseModel, db

class CustomerModel(BaseModel):
    __tablename__ = 'customer'
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    address = db.Column(db.String(50), nullable=True)
    email_address = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    is_verified = db.Column(db.Boolean(), default=False)

    def as_dict(self):
        restricted_keys = ['password', 'id']
        data_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name not in restricted_keys}
        return data_dict

    def basic_data(self):
        keys = ["first_name", "last_name", "dob", "address", "email_address"]
        data_dict = {key: getattr(self, key) for key in keys}
        return data_dict