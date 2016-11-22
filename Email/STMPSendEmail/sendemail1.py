#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:升级版1 带主题 等
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/22.14:50
"""
'''
仔细观察StmpSendEmail.py，发现如下问题：

    邮件没有主题；
    收件人的名字没有显示为友好的名字，比如Mr Green <green@example.com>；
    明明收到了邮件，却提示不在收件人中。

这是因为邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中的，
所以，我们必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件：'''

from email import encoders
from email.header import Header
from  email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib

# parseaddr不是内置函数,见于email.utils, 用来解析字符串中的email地址
# >>> import email.utils
# >>> email.utils.parseaddr('tim_spac@126.com')
# ('', 'tim_spac@126.com')
# >>> email.utils.parseaddr('"Lao Wang" <tim_spac@126.com>')
# ('Lao Wang', 'tim_spac@126.com')

def _format_addr(s):
    name,addr = parseaddr(s)
    print(name,addr)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

# from_addr = 'set@aliyun.com'
# password = '******'
# to_addr = '66***28@qq.com'
# smtp_server = 'smtp.aliyun.com'

# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 发送HTML邮件
#
# 如果我们要发送HTML邮件，而不是普通的纯文本文件怎么办？方法很简单，在构造MIMEText对象时，把HTML字符串传进去，
# 再把第二个参数由plain变为html就可以了：

msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.class.pub">Ronny Website</a>...</p>' +
    '</body></html>', 'html', 'utf-8')



msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)

msg['To'] = _format_addr('管理员 <%s>' % to_addr)
print(msg['From'])
print(msg['To'])
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()