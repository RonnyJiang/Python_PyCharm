#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:条件判断if...elif....else...使用，切记加冒号
 @author: Ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/6.16:04
 """

##因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。
# Python提供了int()函数来完成这件事情，所以定义了一个变量接string
strage= input("请输入你的年龄：")
type(strage)
age = int(strage)
if age>=18:
    print("adult")
elif age>=6:
    print("teenager")
else:
    print("kid")
print(int(input("我的学号：")))
print(type(int(input("我的id："))))  #输入数字后，将纯数字的字符串转化成int类型，并打印数据类型
