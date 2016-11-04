#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改,也没有append()，insert()这样的方法
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/3.12:47
 """
students=('lilei','hanmeimei','ronny')
print(students)
print('one:',students[0],'two:',students[1],'three:',students[2])

#定义一个空tuple
t = ()
print(t)
#定义含有一个元素的tuple（元组）,要在后面加一个逗号，因为括号()既可以表示tuple，又可以表示数学公式中的小括号，有歧义
t = (9,)
print(t)
#tuple是元素成员不能变，lily就是lily，不能变成lucy，指向的地址不能变。但是里面元素若是个变量列表，它就可以变了，eg：
t1 = ('a','b',['A','B'])
print(t1)      #echo : ('a', 'b', ['A', 'B'])
t1[2][0]='Ronny'
t1[2][1]='Jiang'
print(t1)      #echo : ('a', 'b', ['Ronny', 'Jiang'])
####但是这样也只是里面的元素值可以变，长度无法修改，换另一种尝试
lista = ['X','Y','Z']
t2 = ('a','b',lista)
print(t2)     #echo : ('a', 'b', ['X', 'Y', 'Z'])
#这是改变lista，就可以实现更t2元组中的list的目的了
lista.append('ohyeah')
print(t2)     #echo : ('a', 'b', ['X', 'Y', 'Z', 'ohyeah'])

###但是如果我们输入的元素也是一个定义的变量列表，那就没太大意思了。因为list完全可以胜任。
# 学到这我的理解是tuple的意义是类似于我们的枚举一样。只是这个枚举更便捷。不会被修改。
week = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
print(week[-1])
#week[-1]='7'   这样就会报错了,good,就是要利用好这个特征，和list明显的区别---定长、元素不可修改。（除非元素是变量）

######元素是单纯的变量依然不可以通过改变元素指向的地址，因为指向的直接是元素中字符串的地址。
# 而之后变量修改了，元素指向的地址还是之前字符串的地址，而修改的变量指向了一个新的字符串常量地址，用指针的思维就ok了
a1 = 'monday'
a2 = 'tuesday'
weektest = (a1,a2)
print(weektest)
a2 = a2 + 'haha'
print(a2)
print(weektest)
