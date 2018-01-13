from flask import Blueprint
from flask import render_template

main = Blueprint('main', __name__)

# 记得把写在别的地方的路由导入进来
from . import views, errors

