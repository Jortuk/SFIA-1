import unittest

from flask import abort, url_for
from flask_testing import TestCase

from application import app, db, bcrypt
from application.models import Users, Shoes, Shops, ShoesShops
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database

        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        hashed_pw = bcrypt.generate_password_hash('admin2020')
        admin = Users(user_name="testadmin", email="admin@admin.com", password=hashed_pw)

        #create shop inside Shops table
        shop1 = Shops(shop_address="1 Test Address", shop_city="Test City")
        shop2 = Shops(shop_address="2 Test Address", shop_city="Test2City")

        #create shoe inside Shoes table
        shoe1 = Shoes(shoe_name="testshoe1", shoe_size="S", shoe_price="39.99")
        shoe2 = Shoes(shoe_name="testshoe2", shoe_size="S", shoe_price="39.99")
        shoe3 = Shoes(shoe_name="testshoe3", shoe_size="S", shoe_price="39.99")

        #create shoe inside ShoesShops table
        shoeshop1 = ShoesShops(quantity=1, shoe_id=2, shop_id=1)
        shoeshop2 = ShoesShops(quantity=2, shoe_id=3, shop_id=2)

        #save data to database
        db.session.add(admin)
        db.session.add(shop1)
        db.session.add(shop2)
        db.session.add(shoe1)
        db.session.add(shoe2)
        db.session.add(shoe3)
        db.session.add(shoeshop1)
        db.session.add(shoeshop2)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_shoes_view(self):
        response = self.client.get(url_for('shoes'))
        self.assertEqual(response.status_code, 200)

    def test_shops_view(self):
        response = self.client.get(url_for('shops'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

    def test_shop1_view(self):
        response = self.client.get(url_for('shop1'))
        self.assertEqual(response.status_code, 200)

    def test_shop2_view(self):
        response = self.client.get(url_for('shop2'))
        self.assertEqual(response.status_code, 200)

    def test_shop3_view(self):
        response = self.client.get(url_for('shop3'))
        self.assertEqual(response.status_code, 200)

    def test_shop4_view(self):
        response = self.client.get(url_for('shop4'))
        self.assertEqual(response.status_code, 200)

    def test_shop5_view(self):
        response = self.client.get(url_for('shop5'))
        self.assertEqual(response.status_code, 200)

class TestAuthenticatedViews(TestBase):

    def test_shoesadmin_view(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            response = self.client.get(url_for('shoesadmin'))
            self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            response = self.client.get(url_for('logout'))
            self.assertEqual(response.status_code, 302)

    def test_shoe_add_view(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            response = self.client.get(url_for('addShoe'))
            self.assertEqual(response.status_code, 200)

    def test_shoe_update_view(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            shoe = Shoes.query.first()
            response = self.client.get(url_for('updateShoe',id=1))
            self.assertEqual(response.status_code, 200)

    def test_shoe_delete_view(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            shoe = Shoes.query.first()
            response = self.client.get(url_for('deleteShoe',id=1))
            self.assertEqual(response.status_code, 302)

    def test_shop1admin_view(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            response = self.client.get(url_for('shop1admin'))
            self.assertEqual(response.status_code, 200)

    def test_shop2admin_view(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            response = self.client.get(url_for('shop2admin'))
            self.assertEqual(response.status_code, 200)

    def test_shop3admin_view(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            response = self.client.get(url_for('shop3admin'))
            self.assertEqual(response.status_code, 200)

    def test_shop4admin_view(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            response = self.client.get(url_for('shop4admin'))
            self.assertEqual(response.status_code, 200)

    def test_shop5admin_view(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            response = self.client.get(url_for('shop5admin'))
            self.assertEqual(response.status_code, 200)

    def test_updateshop1_view(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            shoeshop = ShoesShops.query.first()
            response = self.client.get(url_for('updateShop1',id=2))
            self.assertEqual(response.status_code, 200)

    def test_updateshop2_view(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            shoeshop = ShoesShops.query.first()
            response = self.client.get(url_for('updateShop2',id=2))
            self.assertEqual(response.status_code, 200)

    def test_updateshop3_view(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            shoeshop = ShoesShops.query.first()
            response = self.client.get(url_for('updateShop3',id=2))
            self.assertEqual(response.status_code, 200)

    def test_updateshop4_view(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            shoeshop = ShoesShops.query.first()
            response = self.client.get(url_for('updateShop4',id=2))
            self.assertEqual(response.status_code, 200)

    def test_updateshop5_view(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            shoeshop = ShoesShops.query.first()
            response = self.client.get(url_for('updateShop5',id=2))
            self.assertEqual(response.status_code, 200)

class TestPosts(TestBase):

    def test_add_new_shoe(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            response = self.client.post(
                url_for('addShoe'),
                data=dict(
                    shoe_id=4,
                    shoe_name="Test",
                    shoe_size="S",
                    shoe_price=40
                ),
            follow_redirects=True
            )
            self.assertIn(b'Test', response.data)

    def test_update_shoe(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            response = self.client.post(
                url_for('updateShoe',id=1),
                data=dict(
                    shoe_name="UpdateTest",
                    shoe_price=12.34
                ),
            follow_redirects=True
            )
            self.assertIn(b'UpdateTest', response.data)

    def test_update_shop1(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            response = self.client.post(
                url_for('updateShop1',id=2),
                data=dict(
                    quantity="4"
                ),
            follow_redirects=True
            )
            self.assertIn(b"4", response.data)

    def test_update_shop2(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            response = self.client.post(
                url_for('updateShop2',id=2),
                data=dict(
                    quantity="2"
                ),
            follow_redirects=True
            )
            self.assertIn(b"2", response.data)

    def test_update_shop3(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            response = self.client.post(
                url_for('updateShop3',id=2),
                data=dict(
                    quantity="1"
                ),
            follow_redirects=True
            )
            self.assertIn(b"1", response.data)

    def test_update_shop4(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            response = self.client.post(
                url_for('updateShop4',id=2),
                data=dict(
                    quantity="10"
                ),
            follow_redirects=True
            )
            self.assertIn(b"10", response.data)

    def test_update_shop5(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email="admin@admin.com",
                    password="admin2020"
                ),
            follow_redirects=True
            )
            response = self.client.post(
                url_for('updateShop5',id=2),
                data=dict(
                    quantity="3"
                ),
            follow_redirects=True
            )
            self.assertIn(b"3", response.data)






    
 

# class TestPosts(TestBase):

 

#     def test_add_new_post(self):
#         """
#         Test that when I add a new post, I am redirected to the homepage with the new post visible
#         """
#         with self.client:
#             response = self.client.post(
#                 '/post',
#                 data=dict(
#                     title="Test Title",
#                     content="Test Content"
#                 ),
#                 follow_redirects=True
#             )
#             self.assertIn(b'Test Title', response.data)