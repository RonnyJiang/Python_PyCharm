#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: 调用其他py文件的函数
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/7.13:43
"""

from definefunctions import my_abs     #调用definefunctions.py文件中的my_abs方法  .py后缀在调用时省略掉
print(my_abs(-100))

from definefunctions import my_max     #调用definefunctions.py文件中的my_max方法
print(my_max(3,8))

