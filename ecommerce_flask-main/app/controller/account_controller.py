from flask import Blueprint, render_template, session
import pickle

from app.model.account import Account

account_bp = Blueprint('account', __name__)

@account_bp.route('/account')
def account():
    return render_template('account.html')



@account_bp.route('/')
def view_account():
    account = session.get('account', Account())
    if isinstance(account, bytes):
        account = pickle.loads(account)
    return render_template('account.html', account=account)