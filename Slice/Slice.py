#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:切片，截取数据段很好用
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/8.12:11
"""

"""

取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：

>>> L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

取前3个元素，应该怎么做？

笨办法：

>>> [L[0], L[1], L[2]]
['Michael', 'Sarah', 'Tracy']

之所以是笨办法是因为扩展一下，取前N个元素就没辙了。

取前N个元素，也就是索引为0-(N-1)的元素，可以用循环：

>>> r = []
>>> n = 3
>>> for i in range(n):
...     r.append(L[i])
...
>>> r
['Michael', 'Sarah', 'Tracy']

"""
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前3个元素，用一行代码就可以完成切片：
print(L[0:3])   #echo : ['Michael', 'Sarah', 'Tracy']
##L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。

# 如果第一个索引是0，还可以省略：
print(L[:3])    #前三个元素['Michael', 'Sarah', 'Tracy']
# 也可以从索引1开始，取出2个元素出来：
print(L[1:3])   #echo : ['Sarah', 'Tracy']
# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：
print(L[-2:])   #echo :['Bob', 'Jack']
"""
记住倒数第一个元素的索引是-1。
切片操作十分有用。我们先创建一个0-99的数列：
"""
listA = list(range(100))
print(listA)
# 可以通过切片轻松取出某一段数列。比如前10个数：
print(listA[:10])
#后10个数：
print(listA[-10:])
# 前11-20个数：
print(listA[11:20])
# 前10个数，每两个取一个：
print(listA[:10:2])
# 所有数，每5个取一个：
print(listA[::5])
# 甚至什么都不写，只写[:]就可以原样复制一个list：
print(listA[:])
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
tupleA = tuple(range(5))
print(tupleA)
tupleB = tupleA[:3]    ##只会产生中间值，然后赋值给tupleB，tupleA的值是字符串常量，不会变。
print(tupleA)          #echo (0, 1, 2, 3, 4)
print(tupleB)          #echo (0, 1, 2)

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
strA = 'ABCDEF'
strB = strA[::2]
print(strA)
print(strB)


#####练习，先猜测输出结果，在看看预期的结果和实际结果是否有出处
L2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L2)           #前六个都是相等的，第一个为开始索引，默认为0，第二个为结束索引，默认为len（list），
print(L2[:])        #第三个为方向和间隔，正数为正向遍历，负数为反向遍历，数的绝对值为遍历间隔
print(L2[0:])
print(L2[0:len(L2)])
print(L2[::])
print(L2[::1])       #PRE ECHO: [1,2,3,4,5,6,7,8,9]  #前两两个什么都没有，即遍历整个list；最后为1，即正向遍历，间隔为1
print(L2[::-1])      #PRE ECHO: [9,8,7,6,5,4,3,2,1]  #前两两个什么都没有，即遍历整个list；最后为-1，即反向遍历，间隔为1
print(L2[:8:1])      #PRE ECHO: [1,2,3,4,5,6,7,8] #第一个为空，即从0开始；第三个为1，即正向遍历，间隔为1；
print(L2[-2::1])     #PRE ECHO: [8,9]  从倒数第二个元素开始，看最后的是1，即正向遍历，间隔为1；中间为空，即遍历到结束。8开始到9ok
print(L2[-2::-1])    #PRE ECHO: [8,7,6,5,4,3,2,1]从倒数第二个元素开始；看最后的是-1，即反向遍历，间隔为1；中间为空，即遍历到结束。
print(L2[-2:0:-1])   #PRE ECHO: [8,7,6,5,4,3,2]从倒数第二个元素开始；看最后的是-1，即反向遍历，间隔为1；中间为0，即遍历到0，且不包含0
print(L2[-2:0:-2])   #PRE ECHO: [8,6,4,2]   从倒数第二个元素开始，看最后的是-2，即反向遍历,间隔为2，中间为0，即遍历到0，且不包含0

