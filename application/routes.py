from flask import render_template, redirect, url_for
from application import app, db

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home Page")
