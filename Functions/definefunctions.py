#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: 自定义函数
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/7.13:34
"""

###Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:   注意要加冒号
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回。
#①定义普通函数
def my_abs(x):
    if x >= 0 :
        return x
    else :
        return  -x
# print(my_abs(-8))
# print(my_abs(3.14))
# print(my_abs(0))
# print(my_abs(int('123')))
def my_max(a,b):
    if a>=b:
        return a
    else:
        return b
#如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
# return None可以简写为return。
# 如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，
# 用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）
#eg ：看test.py中对my_abs()函数的调用  from definefuctions import my_abs

#②定义空函数
#空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass
# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，
# 比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
# pass还可以用在其他语句里，比如：
age = 19
if age >= 18:
    pass
# 缺少了pass，代码运行就会有语法错误。

#③参数检查
####!!!!!!!!!!!!!!参数检查!!!!!!!!!!!!!!!!!
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
# print(my_abs(1,2))   #echo : TypeError: my_abs() takes 1 positional argument but 2 were given
# 但是如果参数类型不对，Python解释器就无法帮我们检查。试试my_abs和内置函数abs的差别：
# print(my_abs('a'))   #TypeError: unorderable types: str() >= int()
#print(abs('a'))        #TypeError: bad operand type for abs(): 'str'

##当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，
# 出错信息和abs不一样。所以，这个函数定义不够完善。

#让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
def my_new_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type for abs() : %s' % type(x))
        ##如果是字符串则输出：TypeError: bad operand type for abs() : <class 'str'>
    if x >= 0:
        return x
    else :
        return -x

#print(my_new_abs('a'))    ##echo：TypeError: bad operand type for abs() : <class 'str'>
#错误和异常处理将在后续研究。


