from flask import render_template
from app.prices import bp

@bp.route("/")
def login():
    return render_template("index.html")