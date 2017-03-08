#coding:utf8
#create by zhouyao 
#data: $

from __future__ import unicode_literals
from flask_wtf import Form
from flask_babel import _
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Length, Email, EqualTo


class LoginForm(Form):
    username = StringField(_("用户名"), validators=[Required(), Length(1, 64)])
    password = PasswordField(_("密码"), validators=[Required()])
    submit = SubmitField(_("提交"))


class RegisterForm(Form):
    username = StringField(_("用户名"), validators=[Required(), Length(1, 64)])
    password = PasswordField(_("密码"), validators=[Required(),EqualTo("password2",message="tesssss")])
    password2 = PasswordField(_("请再输入一次"), validators=[Required()])
    submit = SubmitField(_("提交"))

class PersoninfoForm(Form):
    username = StringField(_("用户名"),validators=[Required(),Length(1,64)])
    nick_name = StringField(_("昵称"),validators=[Required(),Length(1,64)])
    birth_day = StringField(_("出生日期"),validators=[Required(),Length(1,64)])
    phone = StringField(_("主要电话"),validators=[Required(),Length(1,64)])
    phone2 = StringField(_("备用电话"),validators=[Required(),Length(1,64)])
    photo = StringField(_("显示图片"),validators=[Required(),Length(1,64)])
    address = StringField(_("家庭地址"),validators=[Required(),Length(1,64)])
    submit = SubmitField(_("提交"))