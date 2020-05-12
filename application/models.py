from application import db

class Shoes(db.Model):
    __tablename__ = 'shoes'
    shoe_id = db.Column(db.Integer, primary_key=True)
    shoe_name = db.Column(db.String(30), nullable=False, unique=True)
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
