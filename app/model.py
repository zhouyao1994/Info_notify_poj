# coding:utf8
# create by zhouyao
# data: $

from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from . import login
from flask_login import UserMixin


class User(UserMixin, db.Model):
    ___tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError("password is not readable")

    @password.setter
    def password(self, passw):
        self.password_hash = generate_password_hash(passw)

    def virify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(username):
    return User.query.get(username)


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
