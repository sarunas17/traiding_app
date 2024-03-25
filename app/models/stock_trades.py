from app.extensions import db
from datetime import datetime

class StockTrades(db.Model):
    __tablename__ = "stock_trades"
    id = db.Column(db.Integer, primary_key=True)
    stock_name = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float)
    amount = db.Column(db.Integer)
    createdAt = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User")