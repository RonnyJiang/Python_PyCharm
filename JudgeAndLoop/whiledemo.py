#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
 @author: Ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/6.16:05
 """
#计算100以内所有奇数之和，可以用while循环实现：
num1 = 99
sum1 = 0
while num1 > 0:
    sum1 = sum1 + num1
    num1 = num1 - 2
print(sum1)