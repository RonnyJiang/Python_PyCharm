#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:sort的练习题  （注：Sort也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。）
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/9.10:28
"""
'''
练习
假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
'''
'''①请用sorted()对上述列表分别按名字排序：'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]
L1 = sorted(L,key=by_name)
print(L1)
L2 = sorted(L, key=by_name,reverse = True)   ##注意不是reversed no ‘d’
print(L2)
'''②再按成绩从高到低排序：'''
def by_score(t):
    return t[1]
L3 = sorted(L,key=by_score)     #成绩从低到高
print(L3)
L4 = sorted(L,key=by_score,reverse = True)    #成绩从高到低
print(L4)