#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: 发邮件时，MUA和MTA使用的协议就是SMTP：Simple Mail Transfer Protocol，后面的MTA到另一个MTA也是用SMTP协议。
        现在的例子即为：利用stmp协议，发送一封邮件
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/22.13:37
"""
# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
#
# 首先，我们来构造一个最简单的纯文本邮件：
from email.mime.text import MIMEText
msg = MIMEText('Hi Harson:\nI miss you.\nsend by RonnyJiang \nSince@python 3.5.3(32bit)...','plain','utf-8')

# 注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，
# 最后一定要用utf-8编码保证多语言兼容性。
#
# 然后，通过SMTP发出去：
# 输入Email地址和口令:
from_addr = input('From:')
password = input('Password:')

## 输入收件人地址:
to_addr = input('To:')
# 输入SMTP服务器地址:
smtp_host = input('SMTP Server:')

import smtplib

server = smtplib.SMTP(host=smtp_host,port=25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。SMTP协议就是简单的文本命令和响应。login()方法用来登录SMTP服务器，
# sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
#
# 如果一切顺利，就可以在收件人信箱中收到我们刚发送的Email：
'''
交互界面
From:set@aliyun.com
Password:**********
To:66****8@qq.com
STMP Server:smtp.aliyun.com

'''
