from _testcapi import NullTpDocType
from flask import render_template, session, redirect, request

from extensions import db, client
from models import User
from app import create_app


app = create_app()
PRODUCTS = {'12345': {'name': 'Gas Mask', 'description': 'old soviet gas mask', 'price': 2000, 'image': '12345.png'}}

@app.route('/')
def index():
    print(session['cart'])
    return render_template('index.html', PRODUCTS=PRODUCTS)

@app.route('/add_to_cart/<product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = {}
    if product_id in session['cart']:
        print('product already here, adding 1')
        session['cart'][product_id]['quantity'] += 1
        session.modified = True
    else:
        session['cart'][product_id] = {
            'name': PRODUCTS[product_id]['name'],
            'price': PRODUCTS[product_id]['price'],
            'quantity': 1
        }
        session.modified = True
    return redirect(request.referrer)
@app.route('/view_cart')
def view_cart():
    if not 'cart' in session:
        session['cart'] = {}
    return render_template('view_cart.html', cart=session['cart'], PRODUCTS=PRODUCTS)

@app.route('/clear_cart')
def clear_cart():
    if not 'cart' in session:
        session['cart'] = {}
    session['cart'] = {}
    return redirect(request.referrer)