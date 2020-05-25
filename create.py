from application import db
from application.models import Shoes, Shops, ShoesShops

db.drop_all()
db.create_all()
