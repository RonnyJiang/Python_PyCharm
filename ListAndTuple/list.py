#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:介绍python内置的数据类型--list，它是一种有序的集合，可以随时添加和删除其中的元素
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/3.12:45
 """

students = ['Lilei','Hanmeimei','Xiaoming','Cuihua']
print (students)
print ('most popular students : %s ,%s' % (students[0],students[3]))
print (students[0],students[3])
#print(students[4]) 会报error，IndexError: list index out of range，提示访问超出范围
#所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。
print(students[len(students)-1])

#python访问列表元素也支持倒叙，索引用负数表示
#需要注意的是最后一个是-1 即n个元素的列表 正序0至n-1，倒序是-1至-n
print(students[-1],students[-2],students[-3]，print(students[-4])
