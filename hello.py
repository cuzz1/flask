# -*- coding:utf-8 -*-
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY']= 'nobody knows i am'
bootstrap = Bootstrap(app)

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

# 定义表单
class NameForm(Form):
	name = StringField("what is your name?", validators=[Required()])
	submit = SubmitField("Submit")




@app.route("/", methods=['GET','POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template("index.html",form=form,name=name)

@app.route("/user/<name>")
def user(name):
    # 后面传的参数必须是字典格式
    return render_template("user.html", name=name) 

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template("500.html"), 500

if __name__ == "__main__":
    config=dict(
            debug=True,
            host="0.0.0.0",
            port=2000,
            )
    app.run(**config)
