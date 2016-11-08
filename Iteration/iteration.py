#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: iterator 迭代器
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/8.14:54
"""
"""
如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
在Python中，迭代是通过for ... in来完成的，而很多语言比如C或者Java，迭代list是通过下标完成的，比如Java代码：
for (i=0; i<list.length; i++) {
    n = list[i];
}
可以看出，Python的for循环抽象程度要高于Java的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：
"""
##迭代字典dict
d = {'a':1,'b':2,'c':3}
for key in d:
    print(key,d[key])    ##每次迭代输出的结果顺序都可能变化


"""
因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
默认情况下，dict迭代的是key。
"""
# 如果要迭代value，可以用for value in d.values()
for value in d.values():
    print(value)
# 如果要同时迭代key和value，可以用for k, v in d.items()。因为默认情况下，dict迭代的是key。
for key,value in d.items():
    print(key,value)
# 由于字符串也是可迭代对象，因此，也可以作用于for循环：
for ch in 'Ronny':
    print(ch)
"""
所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
"""
from collections import Iterable
print(isinstance("abc",Iterable))  # str是否可迭代    echo: True
print(isinstance([1,2,3],Iterable))  # list是否可迭代   echo: True
print(isinstance(('a','b','c'),Iterable))  # tuple是否可迭代  echo: True

print(isinstance(123,Iterable))  # 整数是否可迭代   echo: False
"""最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？
Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身："""

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
#上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：

for x,y in [('Ronny',228),('cici',336),('lili',552)]:   #但是字典不行，字典是分号，需要用for key,value in d.items(): 才行
    print(x,y)

"""
--------------------------------------------------------------------------------------------
小结
任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。
--------------------------------------------------------------------------------------------
"""