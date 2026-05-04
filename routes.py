from flask import render_template, session

from extensions import db
from models import User
from app import create_app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_to_cart/<product_id>')
def add_to_cart(product_id):
    if not session['cart'][product_id]:
        session['cart'][product_id] = 1
    else:
        session['cart'][product_id] = session['cart'][product_id] + 1
