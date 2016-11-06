#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:dict是用空间来换取时间的一种方法。key必须是不可变对象。
 @author: Ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/6.22:56
 """
###tuple元祖是（1，2，3），小括号。元素不可重新赋值（元素是列表了重新赋值），长度len（tuple）不变
###list列表是[1,2,3]，方括号。可写，长度可变，元素可重新赋值
###dict字典是大括号。元素是key-value的形式，key唯一，value可以有相同，长度len可变
d1 = { 'Ronny': 97,'Lily': 31,'Cici': 85 }
print(d1['Ronny'],d1['Cici'])
d1['colin'] = 88   #字典可以动态添加元素，如果名字与之前的key相同，那就是对之前的key进行重新赋值
print(d1)

#如果key不存在，dict就会报错，所以要避免key不存在的错误。
# 有两种办法，
# 一是通过in判断key是否存在：
print('Ronny' in d1)
ifexist = 'Lily' in d1  ##echo True    #如果存在返回True，不存在返回False
print(ifexist)
notexist = 'Lily' not in d1
print(notexist)     ##如果不存在返回True，存在返回False
#二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
ret1 = d1.get('Ronny',-1)   #如果不存在Ronny则返回值是-1。而这里存在，所以返回值不是-1
print(ret1)
ret2 = d1.get('Lucy',-1)    #不存在所以返回值是-1
print(ret2)   #echo -1

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
#请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的
d1.pop('Ronny')
print(d1)
