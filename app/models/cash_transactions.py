from app.extensions import db
from datetime import datetime


class CashTransactions(db.Model):
    __tablename__ = "cash_transactions"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    stock_trade_id = db.Column(db.Integer, db.ForeignKey("stock_trades.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    createdAt = db.Column(db.DateTime, default=datetime.now)
    user = db.relationship("User")