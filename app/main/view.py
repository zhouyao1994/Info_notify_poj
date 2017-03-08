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
    return render_template("News.html", news=all_news, i=len(all_news))

@main.route("/info/get/more_info")
def more_info():
    more_news = News.query.limit(3).offset(3).all()
    # json
    # for new in more_news:

    return more_news
    # print str(News.query.limit(3))
    # print more_news
    # print '查询成功','长度为', more_news.count(),'\n'
    # print '数据类型为',type(more_news)
    #
    # return more_news



@main.route("/info/get/contact")
@login_required
def contact():
    all_contact = Contact.query.all()
    return render_template("Contact.html", contacts=all_contact)


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def page_not_found(e):
    return render_template('404.html'), 500


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
    return render_template("Register.html", form=registerform)


@main.route("/logout")
@login_required
def log_out():
    logout_user()
    flash("you hava log out")
    return redirect(url_for("main.index"))


@main.route("/get")
@login_required
def get_it():
    print "xxxxx"
    return "this is a private page,should login. and now you are logged in ~"
