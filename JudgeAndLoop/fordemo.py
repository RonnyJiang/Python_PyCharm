#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: for x in xs:  for循环
 @author: Ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/6.16:05
 """
names = ['ronny','haiyang','fengqingyang']
for name in names:
    print(name)


#再比如我们想计算1-10的整数之和，可以用一个sum变量做累加：
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

print((range(5)))
##如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，
# 可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
print(list(range(10))) #echo : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sum100 = 0
for i in range(101):
    sum100 = sum100 + i
print(sum100)


######test############################
#请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for j in L:
    print("Hello," + j)

