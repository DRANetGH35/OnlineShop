from flask import render_template, session, redirect

from extensions import db, client
from models import User
from app import create_app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_to_cart/<product_id>')
def add_to_cart(product_id):
    if not session['cart'][product_id]:
        session['cart'][product_id] = 1234
    else:
        session['cart'][product_id] = session['cart'][product_id] + 1

@app.route('/view_cart')
def view_cart():
    return render_template('view_cart.html')