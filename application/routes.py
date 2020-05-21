from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Users, Shoes, Shops, ShoesShops
from application.forms import RegisterForm, LoginForm, UpdateShoeForm, AddShoeForm, UpdateQuantityForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home Page")

@app.route('/shoes')
def shoes():
    shoeData = Shoes.query.all()
    return render_template('shoes.html', title='Shoes', shoes=shoeData)

@app.route('/shoesadmin')
def shoesadmin():
    shoeData = Shoes.query.all()
    return render_template('shoesadmin.html', title='Shoes', shoes=shoeData)

@app.route('/shops')
def shops():
    return render_template('shops.html', title='Shops')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(user_name=form.user_name.data, email=form.email.data, password=hash_pw)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/about')
def about():
    return render_template('about.html', title="About Page")

@app.route('/shoe_add', methods=['GET', 'POST'])
def addShoe():
    form = AddShoeForm()
    if form.validate_on_submit():
        newShoe = Shoes(
            shoe_id = form.shoe_id.data,
            shoe_name = form.shoe_name.data,
            shoe_size = form.shoe_size.data,
            shoe_price = form.shoe_price.data
        )
        db.session.add(newShoe)
        db.session.commit()
        return redirect(url_for('shoesadmin'))
    else:
        print(form.errors)
    return render_template('shoe_add.html', title="Add Shoe", form=form)

@app.route('/shoe_update/<id>', methods=['GET', 'POST'])
def updateShoe(id):
    form = UpdateShoeForm()
    getShoe = Shoes.query.filter_by(shoe_id=id).first()
    if form.validate_on_submit():
        getShoe.shoe_name = form.shoe_name.data
        getShoe.shoe_price = form.shoe_price.data
        db.session.commit()
        return redirect(url_for('shoesadmin'))
    elif request.method == 'GET':
        form.shoe_name.data = getShoe.shoe_name
        form.shoe_price.data = getShoe.shoe_price
    return render_template('shoe_update.html', title="Update Shoe", form=form, shoe=getShoe)

@app.route('/shoe_update/<id>/delete', methods=['GET', 'POST'])
def deleteShoe(id):
    shoe = Shoes.query.filter_by(shoe_id=id).first()
    db.session.delete(shoe)
    db.session.commit()
    return redirect(url_for('shoesadmin'))

@app.route('/shop1', methods=['GET', 'POST'])
def shop1():
    newData = ShoesShops.query.all()
    return render_template('shop1.html', title="4 Aglet Avenue", shoesshops=newData)

@app.route('/shop1admin', methods=['GET', 'POST'])
def shop1admin():
    newData = ShoesShops.query.all()
    return render_template('shop1admin.html', title="4 Aglet Avenue", shoesshops=newData)

@app.route('/update_shop1/<id>', methods=['GET', 'POST'])
def updateShop1(id):
    form = UpdateQuantityForm()
    getQuan = ShoesShops.query.filter_by(shoe_id=id).first()
    if form.validate_on_submit():
        getQuan.quantity = form.quantity.data
        db.session.commit()
        return redirect(url_for('shop1admin'))
    elif request.method == 'GET':
        form.quantity.data = getQuan.quantity
    return render_template('shop_update.html', title="Update Quantity", form=form, x=getQuan)

@app.route('/shop2', methods=['GET', 'POST'])
def shop2():
    newData = ShoesShops.query.all()
    return render_template('shop2.html', title="2 Laces Lane", shoesshops=newData)

@app.route('/shop2admin', methods=['GET', 'POST'])
def shop2admin():
    newData = ShoesShops.query.all()
    return render_template('shop2admin.html', title="2 Laces Lane", shoesshops=newData)

@app.route('/update_shop2/<id>', methods=['GET', 'POST'])
def updateShop2(id):
    form = UpdateQuantityForm()
    getQuan = ShoesShops.query.filter_by(shoe_id=id).first()
    if form.validate_on_submit():
        getQuan.quantity = form.quantity.data
        db.session.commit()
        return redirect(url_for('shop2admin'))
    elif request.method == 'GET':
        form.quantity.data = getQuan.quantity
    return render_template('shop_update.html', title="Update Quantity", form=form, x=getQuan)

@app.route('/shop3', methods=['GET', 'POST'])
def shop3():
    newData = ShoesShops.query.all()
    return render_template('shop3.html', title="1 Pair Place", shoesshops=newData)

@app.route('/shop3admin', methods=['GET', 'POST'])
def shop3admin():
    newData = ShoesShops.query.all()
    return render_template('shop3admin.html', title="1 Pair Place", shoesshops=newData)

@app.route('/update_shop3/<id>', methods=['GET', 'POST'])
def updateShop3(id):
    form = UpdateQuantityForm()
    getQuan = ShoesShops.query.filter_by(shoe_id=id).first()
    if form.validate_on_submit():
        getQuan.quantity = form.quantity.data
        db.session.commit()
        return redirect(url_for('shop3admin'))
    elif request.method == 'GET':
        form.quantity.data = getQuan.quantity
    return render_template('shop_update.html', title="Update Quantity", form=form, x=getQuan)


@app.route('/shop4', methods=['GET', 'POST'])
def shop4():
    newData = ShoesShops.query.all()
    return render_template('shop4.html', title="10 Sole Station", shoesshops=newData)

@app.route('/shop5', methods=['GET', 'POST'])
def shop5():
    newData = ShoesShops.query.all()
    return render_template('shop5.html', title="34 Heel Hill", shoesshops=newData)