# coding:utf8
# create by zhouyao
# data: $
# blueprint 导入设置
from . import main
from flask import render_template, url_for, redirect, flash
from ..model import News, Contact, User
from .. import db
from form import LoginForm, RegisterForm
from flask_login import login_user, logout_user, login_required


@main.route("/")
def index():
    return redirect(url_for("main.news_info"))



@main.route("/info/get/news")
def news_info():
    all_news = News.query.all()
    return render_template("News.html", news=all_news)


@main.route("/info/get/contact")
@login_required
def contact():
    all_contact = Contact.query.all()
    return render_template("contact_table.html", contacts=all_contact)


@main.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@main.route("/test")
def test():
    return redirect(url_for("main.news_info"))


@main.route("/login", methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        user = User.query.filter_by(username=loginForm.username.data).first()
        if user is not None and user.virify_password(loginForm.password.data):
            login_user(user)
            flash("login success")
            return redirect(url_for("main.news_info"))
    return render_template("login.html", form=loginForm)


@main.route("/register", methods=['GET', 'POST'])
def register():
    registerform = RegisterForm()
    if registerform.validate_on_submit():
        user = User(username=registerform.username.data, password=registerform.password.data)
        if not User.query.filter_by(username=registerform.username.data).first():
            db.session.add(user)
            db.session.commit()
            flash("register sucess")
        else:
            flash("has registerec")
    return render_template("register.html", form=registerform)


@main.route("/logout")
@login_required
def log_out():
    logout_user()
    flash("you hava log out")
    return redirect(url_for("main.register"))


@main.route("/get")
@login_required
def get_it():
    print "xxxxx"
    return "this is a private page,should login. and now you are logged in ~"
