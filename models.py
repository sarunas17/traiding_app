import os
from datetime import datetime
from flask_login import UserMixin
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = '4654f5dfadsrfasdr54e6rae'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'traiding.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.now)
    updatedAt = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

class StockTrades(db.Model):
    __tablename__ = "stock_trades"
    id = db.Column(db.Integer, primary_key=True)
    stock_name = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float)
    amount = db.Column(db.Integer)
    createdAt = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User")

class CashTransactions(db.Model):
    __tablename__ = "cash_transactions"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    stock_trade_id = db.Column(db.Integer, db.ForeignKey("stock_trades.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    createdAt = db.Column(db.DateTime, default=datetime.now)
    user = db.relationship("User")

