import os
import unittest

#这是一个基于unittest的一个扩展，
import sys

import time
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner
#str 是string f 是format格式 strtime（）通过这个方法可以定义时间的格式

now=time.strftime("%Y-%m-%d_%H-%M-%S")


def send_mail(path):
    f=open(path,'rb')
    mail_body=f.read()
    f.close()
    #要想发邮件我们把二进制的文件转成MIME（多用途）格式 multpurse Internet Extension 扩展
    #这种格式是对邮件协议的一个拓展，使邮件不仅支持文本格式 ，还支持多种格式，
    msg=MIMEText(mail_body,'html','utf-8')
    msg['subject']=Header("自动化测试报告",'utf-8')


if __name__ == '__main__':
    base_path=os.path.dirname(__file__)
    suite=unittest.defaultTestLoader.discover('./diwutian','*Test.py')
    #文本测试用例运行器 unittest.TextTestRunner().run(suite)
    #html的测试用例会生成一个html的测试报告
    path=base_path+"/report/report"+ now +".html"
    file=open(path,"wb")
    HTMLTestRunner(stream=file, verbosity=1, title="海盗商城测试报告",
                   description="测试环境：windowsever2008+Chrome").run(suite)
    #现在我们的html的测试报告生成了，当测试用例全部执行完成，应该生成一份提醒邮件
    #要把Html报告作为邮件正文发送给
    file.close()
    send_mail(path)



