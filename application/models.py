from application import db, login_manager
from flask_login import UserMixin
from sqlalchemy import ForeignKey

class Shoes(db.Model):
    __tablename__ = 'shoes'
    shoe_id = db.Column(db.Integer, primary_key=True)
    shoe_name = db.Column(db.String(30), nullable=False)
    shoe_size = db.Column(db.String(2), nullable=False)
    shoe_price = db.Column(db.Float, nullable=False)
    shoe = db.relationship('ShoesShops', backref='s1', lazy=True)

    def __repr__(self):
        return ''.join([
            'ID:', str(self.shoe_id)
        ])

class Shops(db.Model):
    __tablename__ = 'shops'
    shop_id = db.Column(db.Integer, primary_key=True)
    shop_address = db.Column(db.String(100), nullable=False, unique=True)
    shop_city = db.Column(db.String(30), nullable=False)
    shop = db.relationship('ShoesShops', backref='s2', lazy=True)

    def __repr__(self):
        return ''.join([
            'ID:', str(self.shop_id)
        ])

class ShoesShops(db.Model):
    __tablename__ = 'shoesShops'
    id = db.Column(db.Integer, primary_key=True)
    shoe_id = db.Column(db.Integer, db.ForeignKey('shoes.shoe_id'), nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.shop_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
    

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n', 'Email: ', self.email])
    def get_id(self):
            return self.id

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
