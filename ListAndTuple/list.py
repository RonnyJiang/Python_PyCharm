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
print(students[-1],students[-2],students[-3],print(students[-4]))

students.append("ronny")
print(students[-1])

students.insert(2,['haiyang','harson']) #在下标为2插入一个元素，这个元素本身又是一个列表
print(students)
print(students[2]) #对students[2]不能再调用append，即列表内的列表元素不能再append
print(students[2][0]) #输出下标2中下标为0的元素

##如果列表里的元素是写死的列表，那就不允许修改，它相当于一个‘常量’，而下面的是定义一个变量作为列表。
#列表里存的是变量，所以里面可以变。
sb = ['lele','kaka']
students.append(sb)
print(students)

#students[-1].append()无法调用
sb.append('sasa')
print(sb)
print(students)  #这样students里的也跟着变化了
students.pop() #pop不加参数默认删除尾，加参数eg pop(2) 即删掉下标为2的那个元素

