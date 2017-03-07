# coding:utf8
from __future__ import unicode_literals
from flask import Flask,url_for
import os, json
from flask import (
    g, request, redirect, flash, Response, render_template, Markup)

from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.db")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
db = SQLAlchemy(app)


class Contact(db.Model):
    """
    Contact 模型
    """
    __tablename__ = 'contact'
    contact_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    student_id = db.Column(db.String(20))
    phone = db.Column(db.String(15))
    room_id = db.Column(db.String(20))
    is_roon_leader = db.Column(db.String(2))
    gender = db.Column(db.String(2))
    address = db.Column(db.String(50))

    def get_json(self):
        formate_jsson = {'contact_id': self.contact_id,
                         'name': self.name,
                         'student_id': self.student_id,
                         'room_id': self.room_id,
                         'phone': self.phone,
                         'is_roon_leader': self.is_roon_leader,
                         'gender': self.gender,
                         'address': self.address}
        return formate_jsson


class News(db.Model):
    """
    news模型
    """
    id = db.Column(db.String, primary_key=True)
    post_time = db.Column(db.String(20))
    post_nickname = db.Column(db.String(20))
    news_title = db.Column(db.String(150))
    news_content = db.Column(db.String(1000))
    end_time = db.Column(db.String)

    def get_json(self):
        formate_jsion = {
            'end_time': self.end_time,
            "post_time": self.post_time,
            "post_nickname": self.post_time,
            "news_titile": self.news_title,
            "news_content": self.news_content
        }
        return formate_jsion


@app.route("/")
def index():
    return redirect(url_for("news_info"))


@app.route("/info/get/news")
def news_info():
    all_news = News.query.all()
    return render_template("News.html", news=all_news)


@app.route("/info/get/contact")
def contact():
    contact_json = []
    all_contact = Contact.query.all()
    # for x in all_contact:
    #     contact_json.append(x.get_json())
    # rs_json= json.dumps(contact_json, ensure_ascii=False)
    return render_template("Materialize1.html",news = all_contact)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route("/test")
def test():
     return redirect(url_for("news_info"))


@app.route("/tonggao")
def test2():
    return render_template("Materialize1.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
