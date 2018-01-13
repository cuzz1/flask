from flask import render_template, redirect, url_for, session

from . import main
from .forms import NameForm
from .. import db
from ..models import User

@main.route("/", methods=["GET","POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            seddion["known"] = False
        else:
            session["known"] = True
        session["name"] = form.name.data
        form.name.data = ""
        return redirect(url_for("index"))
    return render_template("index.html",
                           form = form,
                           name = session.get("name"),
                           know = session.get("known", False))

    # return render_template("index1.html", form=form)
