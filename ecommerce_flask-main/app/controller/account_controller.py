from flask import Blueprint, render_template, session
import pickle

from app.model.account import Account

account_bp = Blueprint('account', __name__)

@account_bp.route('/account')
def account():
    return render_template('account.html')



@account_bp.route('/')
def view_account():
    cart = session.get('cart', Account())
    if isinstance(cart, bytes):
        cart = pickle.loads(cart)
    return render_template('cart.html', cart=cart)