from flask import render_template, Blueprint, url_for, request, redirect
from app.utils import admin_required

main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")