from flask import Blueprint

bp = Blueprint('stock_trades', __name__)

from app.stock_trades import routes