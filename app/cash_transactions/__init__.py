from flask import Blueprint

bp = Blueprint('cash_transactions', __name__)


from app.cash_transactions import routes