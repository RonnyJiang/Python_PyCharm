#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: 将用户的用户名明文存储，密码已MD5的形式存储，在登录后去匹配用户密码的MD5值，而不是单纯的去匹配
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/21.16:41
"""
'''
练习

根据用户输入的口令，计算出存储在数据库中的MD5口令：

def calc_md5(password):
    pass

存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。

设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '21218cca77804d2ba1922c33e0151105',
    'alice': '5f4dcc3b5aa765d61d8327deb882cf99'
}

def login(user, password):
    pass

采用MD5存储口令是否就一定安全呢？也不一定。假设你是一个黑客，已经拿到了存储MD5口令的数据库，如何通过MD5反推用户的明文口令呢？
暴力破解费事费力，真正的黑客不会这么干。

考虑这么个情况，很多用户喜欢用123456，888888，password这些简单的口令，于是，黑客可以事先计算出这些常用口令的MD5值，得到一个反推表：

'e10adc3949ba59abbe56e057f20f883e': '123456'
'21218cca77804d2ba1922c33e0151105': '888888'
'5f4dcc3b5aa765d61d8327deb882cf99': 'password'

这样，无需破解，只需要对比数据库的MD5，黑客就获得了使用常用口令的用户账号。

对于用户来讲，当然不要使用过于简单的口令。但是，我们能否在程序设计上对简单口令加强保护呢？

由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，
这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：

def calc_md5(password):
    return get_md5(password + 'the-Salt')

经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。

但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，这说明这两个用户的口令是一样的。
有没有办法让使用相同口令的用户存储不同的MD5呢？

如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。'''
import hashlib
from collections import defaultdict
def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(str(password).encode('utf-8'))
    return md5.hexdigest()

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '21218cca77804d2ba1922c33e0151105',
    'alice': '5f4dcc3b5aa765d61d8327deb882cf99'
}
#michael bob alice密码分别为123456,88888,8，password
def login(user, password):
    passwordmd5 = calc_md5(password)
    print(user,passwordmd5)
    if user in db:
        print('用户名存在，开始校验密码')
        if passwordmd5 == db[user]:
            print('%s,登陆成功' % user)
        else:
            print('登录失败!密码不正确.')
    else:
        print('用户名不存在！')




login('michael','1234567')
login('bob','888888')
login('alice1','password1')


'''
michael fcea920f7412b5da7be0cf42b8c93759
用户名存在，开始校验密码
登录失败!密码不正确.
bob 21218cca77804d2ba1922c33e0151105
用户名存在，开始校验密码
bob,登陆成功
alice1 7c6a180b36896a0a8c02787eeafb0e4c
用户名不存在！
'''

# 练习
#
# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
#
# db = {}
#
# def register(username, password):
#     db[username] = get_md5(password + username + 'the-Salt')
#
# 然后，根据修改后的MD5算法实现用户登录的验证：
#
# def login(username, password):
#     pass
#
# 小结
#
# 摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），
# 只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
