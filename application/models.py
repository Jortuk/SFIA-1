from application import db, login_manager
from flask_login import UserMixin

class Shoes(db.Model):
    __tablename__ = 'shoes'
    shoe_id = db.Column(db.Integer, primary_key=True)
    shoe_name = db.Column(db.String(30), nullable=False)
    shoe_size = db.Column(db.String(2), nullable=False)
    shoe_price = db.Column(db.Float(6), nullable=False)

    def __repr__(self):
        return ''.join([
            'Name: ', self.shoe_name, ' ', 'Size: ', self.shoe_size, '\r\n',
            'Price: ', self.shoe_price
        ])

class Shops(db.Model):
    __tablename__ = 'shops'
    shop_id = db.Column(db.Integer, primary_key=True)
    shop_address = db.Column(db.String(100), nullable=False, unique=True)
    shop_city = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return ''.join([
            'Address: ', self.shop_address, ', ', self.shop_city
        ])

class ShoesShops(db.Model):
    __tablename__ = 'shoesShops'
    id = db.Column(db.Integer, primary_key=True)
    shoe_id = db.Column(db.Integer, db.ForeignKey('shoes.shoe_id'), nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.shop_id'), nullable=False)

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
