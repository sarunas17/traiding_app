from flask import render_template
from app.cash_transactions import bp

@bp.route("/")
def login():
    return render_template("index.html")