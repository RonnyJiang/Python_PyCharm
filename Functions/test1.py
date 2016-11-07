#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:练习 求一元二次方程x的解   ax^2 + bx + c = 0
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/7.15:07
"""

import math

def quadratic(a,b,c):     #quadratic-->二次方程式   descriminant-->判别式
    for elements in (a,b,c):
        if not isinstance(elements,(float,int)):
            raise TypeError('bad operand type,Please input correct parameters')
    descriminant = math.pow(b,2) - 4*a*c
    if descriminant < 0:
        return "no solution"
    else:
        x1 = None
        x2 = None
        if descriminant == 0 :
            x1 = x2 = (-b)/(2*a)
        else :
            x1 = (-b+math.sqrt(descriminant))/(2*a)
            x2 = (-b-math.sqrt(descriminant))/(2*a)
        return x1,x2

##调用函数
print(quadratic(1,3,2))   #(-1.0, -2.0)
print(quadratic(1,1,2))   #no solution
print(quadratic(3,4,5))   #no solution

