#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:字符串和编码demo
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49
 """
# ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节。
# 字母A用ASCII编码是十进制的65，二进制的01000001；
# 字符0用ASCII编码是十进制的48，二进制的00110000，注意字符'0'和整数0是不同的；
# 汉字中已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制的01001110 00101101。
# 你可以猜测，如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，因此，A的Unicode编码是00000000 01000001。
# 新的问题又出现了：如果统一成Unicode编码，乱码问题从此消失了。
# 但是，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。
# 所以，本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。
# UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。
# 如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间：

#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print (ord('A'))
print (chr(98))

#str通过encode()方法可以编码为指定的bytes,如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
print('XYZ'.encode('ascii'))
print('中文'.encode('utf-8'))

x = b'ABC'
print(x.decode('ascii'))   #decode 解码,把单个字节符转成字符串,decode()中参数为源字节码的类型，这个字节码ABC是ascii
# 或者
print(b'def'.decode('ascii'))

y = b'\xe4\xb8\xad\xe6\x96\x87'  #utf-8 的‘中文’两字
print(y.decode('utf-8'))
# 或者
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

#str的长度可以由len函数获取
print(len(y))   #y为字节码所以为长度为6
print(len(y.decode("utf-8")))   #decode后解码为utf-8 的‘中文’两字，故长度为2

print('I\'m a student')
print('''a
b
c''')     #多行输出用三个单引号或双引号括上









