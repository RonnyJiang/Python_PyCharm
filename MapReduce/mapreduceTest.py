#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:mapreduce的练习题
 @author: Ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/9.0:59
"""
'''练习①：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。'''
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return str(name).lower().capitalize()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


'''练习②：Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：'''
# -*- coding: utf-8 -*-

from functools import reduce

def prod(L):
    def multiple(x,y):
        return x*y
    return reduce(multiple,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

print(3*5*7*9)  #945 一致

print(pow(2,3))


'''练习③：利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：'''
# 此题有待完善
from functools import reduce
print(float("30"))
def str2float(s):
    if type(eval(s))==float:
        if '.' in s:
            if  s.endswith('.'):
                return int(s[:len(s)-1]) * 1.0
            n = s.find('.')
            return reduce(lambda x, y: x + y, [reduce(lambda x, y: x * 10 + y, map(int, s[:n])),
                                               reduce(lambda x, y: x * 10 + y, map(int, s[n + 1:])) / pow(10, len(
                                              s) - n - 1)])
        else:
            return int(s)
    elif s.isdigit():
        return int(s)*1.0
    else:
        raise TypeError("bad parameters type")

print(str2float('123854562314.0001'))
print(str2float('30.'))
print(str2float('39'))   #这个还有问题
# print(str2float("-10.15"))  负的浮点数还没考虑