from flask import render_template, sssion, redirect, url_for

from . import main
#from .forms import NameForm
#from .. import db
#from ..models import User

@main.route("/", methods=["GET, POST"])
def index():
    print("test*********")
    return render_template("index1.html")
