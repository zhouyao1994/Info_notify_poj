# coding:utf8
# create by zhouyao
# data: $
# -*- coding: utf-8 -*-
import requests
import json

SIGOL_MESSAGE_URL = "http://sms-api.luosimao.com/v1/send.json"
MUTI_MESSAGE_URL = "http://sms-api.luosimao.com/v1/send_batch.json"
ACCOUNT_STATE_URL = "http://sms-api.luosimao.com/v1/status.json"

AUTH = ("api", "key-9fdabcb605e39b8d623a8592e19a700c")

NOTIFY_SIGN = "【计算机系通知】"

class Message():
    """
    用来发送单个消息的消息对象，初始化参数有
    phone：手机号码
    message:需要发送的主体内容
    sign:结尾签名，必须在螺丝帽账号中先注册再使用
    sign 定义为全局变量。因为个数很少。
    """

    def __init__(self, phone, message, sign,auth):
        self.phone = phone
        self.message = message
        self.sign = sign
        self.auth = auth

    def get_data_to_send(self):
        """
        构造符合api的数据对象
        :return:
        """
        data_to_send = {
            "mobile": self.phone,
            "message": str(self.message) + self.sign
        }
        return data_to_send

    def send_one_message(self):
        """发送当前消息，并打印发送结果"""
        resp = requests.post(url=SIGOL_MESSAGE_URL,
                             auth=self.auth,
                             data=self.get_data_to_send(),
                             timeout=3,
                             verify=False
                             )
        rs_json = json.loads(resp.content)
        print rs_json


class Lot_Message():
    """
    用来批量放松消息的消息对象
    """
    def __init__(self, phone_list, message, sign,auth):
        self.phone_list = phone_list
        self.message = message
        self.sign = sign
        self.auth = auth

    def get_data(self):
        it_phones = self.phone_list
        # 目标
        data_list = ""
        for phone in it_phones:
            data_list += "," + str(phone)
        data = {
            "mobile_list": data_list[1:],
            "message": str(self.message) + self.sign
        }
        return data

    def send_lot_message(self):
        resp = requests.post(url=MUTI_MESSAGE_URL,
                             auth=self.auth,
                             data=self.get_data()
                             )
        print json.loads(resp.content)


def get_account_stat():
    """获取账户状态"""
    resp = requests.get(url=ACCOUNT_STATE_URL,
                        auth=AUTH,
                        timeout=5,
                        verify=False
                        )
    # 返回的rs为str格式 转化为json格式
    rs_json = json.loads(resp.content)
    print "剩余条数: {deposit} ".format(deposit=rs_json["deposit"])


def lsm_send_message(phone, message, sign,auth):
    """封装发送短信接口"""
    if len(phone) > 1:
        mes = Lot_Message(phone_list=phone, message=message, sign=sign,auth=auth)
        mes.send_lot_message()
        print "批量发送"
    else:
        mes = Message(phone=phone, message=message, sign=sign,auth=auth)
        mes.send_one_message()
        print "单个发送"




if __name__ == "__main__":
    phone_list = [13123616850]
    message = "你好，这是周耀发送的测试通知。测试通知。测试通知"
    sign = NOTIFY_SIGN
    lsm_send_message(phone=phone_list, message=message, sign=sign,auth=AUTH)
    get_account_stat()  # print "剩余条数:
