#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
 @author: Ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/6.22:57
 """

#要创建一个set，需要提供一个list作为输入集合：
s = set([1,2,3,])
print(s)   #echo {1, 2, 3}

#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
#添加一个元素
s.add(4)   #添加一个不重复的
print(s)   #echo {1, 2, 3, 4}
s.add(2)   #添加一个重复的，则只有一个存在
print(s)   #echo {1, 2, 3, 4}

#通过remove(key)方法可以删除元素：
s.remove(3)
print(s)   #echo {1, 2, 4}
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)    #echo {2, 3}
print(s1 | s2)    #echo {1, 2, 3, 4}

