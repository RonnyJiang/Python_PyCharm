#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:ListComprehensions --列表生成式，生成复杂的列表，not eg:list(range(10))
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/8.16:03
"""
"""
列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []
for x in range(1, 11):
    L.append(x * x)
但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
"""
lista = [x*x for x in range(1,11)]
print(lista)

'''写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：'''
listb = [x*x for x in range(1,11) if x%2 == 0]
print(listb)

# 还可以使用两层循环，可以生成全排列：
listc = [ m + n for m in "abca" for n in "def"]
print(listc)   #echo:['ad','ae','af','bd','be','bf','cd','ce','cf','ad','ae','af']

"""
三层和三层以上的循环就很少用到了。
运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
"""
import os
listd = [x for x in os.listdir('.')]
print(listd)    #当时在目录下创建了个a.txt 所以echo ：['a.txt', 'ListComprehensions.py']

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：for k, v in d.items(): print(k, '=', v)
# 因此，列表生成式也可以使用两个变量来生成list：
d1 = {'x': 'A', 'y': 'B', 'z': 'C' }
liste = [k + '=' + v for k,v in d1.items()]
print(liste)

#最后把一个list中所有的字符串变成小写：
L1 =  ['Hello', 'World', 'IBM', 'Apple']
listf = [ s.lower() for s in L1]    #将大写变成小写
print(listf)

"""
练习

如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：

>>> L = ['Hello', 'World', 18, 'Apple', None]
>>> [s.lower() for s in L]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <listcomp>
AttributeError: 'int' object has no attribute 'lower'

使用内建的isinstance函数可以判断一个变量是不是字符串：

>>> x = 'abc'
>>> y = 123
>>> isinstance(x, str)
True
>>> isinstance(y, str)
False

请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：

"""
# 期待输出: ['hello', 'world', 'apple']

list1 = ['Hello', 'World', 18, 'Apple', None]
list2 = [ s.lower() for s in list1 if isinstance(s,str) ]
print(list2)


##这个在map reduce那块介绍
def upString(s):
    if isinstance(s,str):
        return s.lower()
    else:
        return s

listg = list(map(upString,list1))
print(listg)