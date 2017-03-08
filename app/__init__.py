#coding:utf8
#create by zhouyao 
#data: $

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import os

basedir = os.path.abspath(os.path.dirname(__file__))
bootstrap = Bootstrap()
db = SQLAlchemy()
login = LoginManager()
login.login_view = 'main.login'  # 没有登录情况下，访问需要登录的页面会跳转到这里，字符串作为url_for参数
login.session_protection = 'strong'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'XXXXXXXXXXXX'
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'data.db')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    bootstrap.init_app(app)
    db.init_app(app)
    login.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    #
    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix="/auth")  # 必须要在这里加上前缀
    return app