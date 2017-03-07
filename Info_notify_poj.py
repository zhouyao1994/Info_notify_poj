# coding:utf8
from __future__ import unicode_literals
from flask import Flask
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
    news_id = db.Column(db.String)
    post_time = db.Column(db.DateTime)
    post_nickname = db.Column(db.String(20))
    news_title = db.Column(db.String(150))
    news_content = db.Column(db.String(1000))

    def get_json(self):
        formate_jsion = {
            'news_id': self.news_id,
            "post_time": self.post_time,
            "post_nickname": self.post_time,
            "news_titile": self.news_title,
            "news_content": self.news_content
        }
        return formate_jsion


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/info/get/news")
def news_info():
    rs = """
    [
{"发送时间":"2016/3/1","标题":"通知聚会1","内容":"1又到一年春天的时候，计划在2-7号，班级举办一次聚会。地点在万宜广场，时间晚上6:30如果不能来请联系周耀","有效期到":"2017/3/7"," 发送人真实姓名":"周耀1","发送人昵称":"住羽光1"},
{"发送时间":"2016/3/2","标题":"通知聚会2","内容":"2又到一年春天的时候，计划在2-7号，班级举办一次聚会。地点在万宜广场，时间晚上6:30如果不能来请联系周耀","有效期到":"2017/3/8"," 发送人真实姓名":"周耀2","发送人昵称":"住羽光2"},
{"发送时间":"2016/3/3","标题":"通知聚会3","内容":"3又到一年春天的时候，计划在2-7号，班级举办一次聚会。地点在万宜广场，时间晚上6:31如果不能来请联系周耀","有效期到":"2017/3/9"," 发送人真实姓名":"周耀3","发送人昵称":"住羽光3"},
{"发送时间":"2016/3/4","标题":"通知聚会4","内容":"4又到一年春天的时候，计划在2-7号，班级举办一次聚会。地点在万宜广场，时间晚上6:31如果不能来请联系周耀","有效期到":"2017/3/10"," 发送人真实姓名":"周耀4","发送人昵称":"住羽光4"},
{"发送时间":"2016/3/5","标题":"通知聚会5","内容":"5又到一年春天的时候，计划在2-7号，班级举办一次聚会。地点在万宜广场，时间晚上6:32如果不能来请联系周耀","有效期到":"2017/3/11"," 发送人真实姓名":"周耀5","发送人昵称":"住羽光5"},
{"发送时间":"2016/3/6","标题":"通知聚会6","内容":"6又到一年春天的时候，计划在2-7号，班级举办一次聚会。地点在万宜广场，时间晚上6:32如果不能来请联系周耀","有效期到":"2017/3/12"," 发送人真实姓名":"周耀6","发送人昵称":"住羽光6"},
{"发送时间":"2016/3/7","标题":"通知聚会7","内容":"7又到一年春天的时候，计划在2-7号，班级举办一次聚会。地点在万宜广场，时间晚上6:33如果不能来请联系周耀","有效期到":"2017/3/13"," 发送人真实姓名":"周耀7","发送人昵称":"住羽光7"},
{"发送时间":"2016/3/8","标题":"通知聚会8","内容":"8又到一年春天的时候，计划在2-7号，班级举办一次聚会。地点在万宜广场，时间晚上6:33如果不能来请联系周耀","有效期到":"2017/3/14"," 发送人真实姓名":"周耀8","发送人昵称":"住羽光8"},

]
    """
    return render_template("news.html", news=rs)

@app.route("/info/get/contact")
def contact():
    contact_json = []
    all_contact = Contact.query.all()
    for x in all_contact:
        contact_json.append(x.get_json())
    # return render_template("contact.html", contact=json.dumps(contact_json, ensure_ascii=False))
    return json.dumps(contact_json, ensure_ascii=False)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route("/")
def  test():
    return render_template("Materialize.html")
@app.route("/tonggao")
def test2():
    return render_template("Materialize1.html")

if __name__ == "__main__":
    app.run(debug=True)