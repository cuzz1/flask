from flask import Blueprint
from flask import render_template

print("&&&&&&&&&&&&&")
main = Blueprint('main', __name__)

#from . import views, errors
@main.route("/", methods=["GET"])
def index():
    return render_template("index1.html")

