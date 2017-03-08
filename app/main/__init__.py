#coding:utf8
#create by zhouyao 
#data: $
#coding:utf8
#create by zhouyao
#data: $

from flask import Blueprint

#注册蓝本的时候，使用url_for 一定要带上，注册蓝本的字符串
main = Blueprint('main',__name__)

from . import view