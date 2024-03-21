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
    name = db.Column("Name", db.String(20), unique=True, nullable=False)
    email = db.Column("Email", db.String(120), unique=True, nullable=False)
    password = db.Column("Password", db.String(60), nullable=False)
    createdAt = db.Column("CreatedAt", db.DateTime, default=datetime.now)
    updatedAt = db.Column("UpdatedAt", db.DateTime, default=datetime.now, onupdate=datetime.now)

class StockTrades(db.Model):
    __tablename__ = "stock_trades"
    id = db.Column(db.Integer, primary_key=True)
    stock_name = db.Column("Stock_name", db.String(20), unique=True, nullable=False)
    price = db.Column("Price", db.Float)
    amount = db.Column("Amount", db.Integer)
    createdAt = db.Column("CreatedAt", db.DateTime, default=datetime.now)
    user_id = db.Column("User_id", db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User")

class CashTransactions(db.Model):
    __tablename__ = "cash_transactions"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column("Amount", db.Float)
    stock_trade_id = db.Column("Stock_trade_id", db.Integer, db.ForeignKey("stock_trades.id"))
    user_id = db.Column("User_id", db.Integer, db.ForeignKey("user.id"))
    createdAt = db.Column("CreatedAt", db.DateTime, default=datetime.now)
    user = db.relationship("User")
