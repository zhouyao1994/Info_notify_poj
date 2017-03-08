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
    username = StringField(_("username"), validators=[Required(), Length(1, 64)])
    password = PasswordField(_("password"), validators=[Required(),EqualTo("password2",message="tesssss")])
    password2 = PasswordField(_("repassword"), validators=[Required()])
    submit = SubmitField(_("submit"))
