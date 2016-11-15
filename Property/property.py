#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: 使用@property装饰器负责把一个方法变成属性调用
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/15.10:47
"""

# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
#
# s = Student()
# s.score = 9999
#
# 这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，
# 这样，在set_score()方法里，就可以检查参数：
class Student(object):
    def get_socre(self):
        return  self.__score

    def set_score(self,value):
        if not isinstance(value,int):
            raise  ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise  ValueError('score must between 0~100')

        self.__score = value


s = Student()
s.set_score(99)
print(s.get_socre())
# s.set_score('1')   #报错


'''但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。
有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！
还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。
Python内置的@property装饰器就是负责把一个方法变成属性调用的：'''

class Student1(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self.__score = value



s1 = Student1()
s1.score = 88    #注意是赋值，不是s1.score(88)
print(s1.score)

# s2 = Student1()
# s2.score = 101   #报不在0~100的错
# print(s2.score)

# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
#
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

class Student2(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
'''
--------------------------------------------------------------------------------------------------------------
小结

@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
--------------------------------------------------------------------------------------------------------------
'''
