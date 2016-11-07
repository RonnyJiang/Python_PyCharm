#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:函数的返回值是一个元组（tuple）
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/7.14:36
"""
# 函数可以返回多个值吗？答案是肯定的。
#
# 比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：
import math
def move(x,y,step,angle=0):
    nx = x + step*math.cos(angle)
    ny = y + step*math.sin(angle)
    return nx,ny

print(move(3,4,6))
print(move(0,0,5,90)) #和自己想的不一样，以为scos（90）为0 sin（90）为1 结果为5,0   但是不是
print(math.cos(90),math.sin(90))   ##-0.4480736161291701 0.8939966636005579
##一查，原来sin(x) \n\n Return the sine of x (measured in radians) 以弧度作为参数
#math.sin(math.radians(90))这样就对了,或者用math.pi  这就是度数了
print(math.cos(math.radians((90))),math.sin(math.radians(90)))    ###
print(move(0,0,5,math.radians(90)))   #echo (3.061616997868383e-16, 5.0)     3.061616997868383e-16为3.0*10的-16次幂==0


x,y = move(100,100,60,math.pi/6)
print(x,y)        #echo :151.96152422706632 130.0

# 但其实这只是一种假象，Python函数返回的仍然是单一值：
position = move(100,100,60,math.pi/6)
print(position)   #echo :151.96152422706632, 130.0)
# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

"""
小结

定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。
"""
