#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: 主要再议不可变对象，字符串常量str是不变对象，而list是可变对象。
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/7.9:55
 """
#对于可变对象，比如list，对list进行操作，list内部的内容是会变化的
listA = [ '2','8','5']
listA.sort()
print(listA)   #echo : ['2', '5', '8']

listA.sort(reverse=True)   ##reverse is True.逆序排列
print(listA)   #echo : ['8', '5', '2']
#如上的listA操作对listA的内部做出了改变

#而对于不可变对象，比如str，对str进行操作呢：

#strA = 'flashall_dtvapp.zip'
###在做签名时根据输入的问签名包来命名签名后的包名。
strA = input("plese input packages name:")
if strA.endswith(".zip"):      #判断字符串以什么结尾
    print("zip file")
else:
    print("file is not zip packages")
    exit(1)
strB = strA.replace(".zip","_signed.zip")
print(strA)   #strA 不变
print(strB)   #strB是 替换后新生成的string，理解为指针指向的地址根本就不同



