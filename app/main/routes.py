from flask import Flask, render_template
from app.main import bp


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/main")
def main():
    return render_template("main.html")


@bp.route("/404")
def page_not_found():
    return render_template("404.html")
