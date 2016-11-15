#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:  使用__slots__
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/14.16:08
"""

# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student(object):
    __slots__ = ('name','age')

s = Student()
s.name = 'Ronny'   # 绑定属性'name'
s.age = 18  # 绑定属性'age'
print(s.name,s.age)
# s.score = 98  # 绑定属性'score' 报错
# 报错
# Traceback (most recent call last):
#   File "C:/python_project/Python_PyCharm/__slots__/__solts__.py", line 21, in <module>
#     s.score = 98
# AttributeError: 'Student' object has no attribute 'score'
'''
由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。

使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
'''
class GeaduateStudent(Student):
    __slots__ = ('score')

g = GeaduateStudent()
g.score = 98
print(g.score)
# g.pp = 'pipi'  报错

g.name = 'gos'
g.age = 1
print(g.score,g.age,g.name)

'''除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。'''