#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/12/8.18:32
"""

'''
了解了WSGI框架，我们发现：其实一个Web App，就是写一个WSGI的处理函数，针对每个HTTP请求进行响应。
但是如何处理HTTP请求不是问题，问题是如何处理100个不同的URL。
每一个URL可以对应GET和POST请求，当然还有PUT、DELETE等请求，但是我们通常只考虑最常见的GET和POST请求。
一个最简单的想法是从environ变量里取出HTTP请求的信息，然后逐个判断：
def application(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    if method=='GET' and path=='/':
        return handle_home(environ, start_response)
    if method=='POST' and path='/signin':
        return handle_signin(environ, start_response)
    ...
只是这么写下去代码是肯定没法维护了。
代码这么写没法维护的原因是因为WSGI提供的接口虽然比HTTP接口高级了不少，但和Web App的处理逻辑比，还是比较低级，我们需要在WSGI接口之上
能进一步抽象，让我们专注于用一个函数处理一个URL，至于URL到函数的映射，就交给Web框架来做。

由于用Python开发一个Web框架十分容易，所以Python有上百个开源的Web框架。这里我们先不讨论各种Web框架的优缺点，直接选择一个比较流行的Web框架——Flask来使用。
用Flask编写Web App比WSGI接口简单（这不是废话么，要是比WSGI还复杂，用框架干嘛？），我们先用pip安装Flask：

$ pip install flask
然后写一个app.py，处理3个URL，分别是：

    GET /：首页，返回Home；
    GET /signin：登录页，显示登录表单；
    POST /signin：处理登录表单，显示登录结果。
注意噢，同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中。
Flask通过Python的装饰器在内部自动地把URL和函数给关联起来，所以，我们写出来的代码就像这样：
'''
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/login',methods=['GET'])
def login_form():
    return '''<form action="/login" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/login',methods=['POST'])
def login():
    #需要从request对象读取表单内容：
    if request.form['username']=='ronny' and request.form['password']=='password':
        return '<h3>Hello, Ronny Jiang!</h3>'
    return '<h3>Bad username or password.</h3>'

@app.route('/tel',methods=['GET'])
def tel():
    return '''<form action="/tel" method="post">
              <h1>tel:136119799*9</h1>
              <p><button type='submit'>i want more</button></p>
              </form>'''

@app.route('/tel',methods=['POST'])
def get_more():
    return '<h1>i can not find more for you</h1>'


if __name__ == '__main__':
    app.run()