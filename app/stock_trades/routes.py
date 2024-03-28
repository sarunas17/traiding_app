from flask import render_template
from app.stock_trades import bp

@bp.route("/")
def login():
    return render_template("index.html")