# -*- coding:utf-8 -*-
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    # 后面传的参数必须是字典格式
    return render_template("user.html", name=name) 

if __name__ == "__main__":
    config=dict(
            debug=True,
            host="0.0.0.0",
            port=2000,
            )
    app.run(**config)
