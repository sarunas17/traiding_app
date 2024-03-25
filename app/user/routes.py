from flask import render_template
from app.user import bp

@bp.route("/login")
def login():
    return render_template("login.html")\
    
@bp.route("/register")
def register():
    return render_template("register.html")


@bp.route("/userprofile")
def userprofile():
    return render_template("userprofile.html")