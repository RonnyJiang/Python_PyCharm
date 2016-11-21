#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/21.16:21
"""

# 我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
# echo (32bit):d26a53750bc40b38b65a520292f69306

# 试试改动一个字母，看看计算的结果是否完全不同。
#
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
#
'''另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：'''
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
print(sha1.hexdigest())
# echo (40bit):80d11a9835ba1f36b995f1e27b5920b42d9c6fdd
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
#
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。
#
# 有没有可能两个不同的数据通过某个摘要算法得到了相同的摘要？完全有可能，因为任何摘要算法都是把无限多的数据集合映射到一个有限的集合中。
# 这种情况称为碰撞，比如Bob试图根据你的摘要反推出一篇文章'how to learn hashlib in python - by Bob'，
# 并且这篇文章的摘要恰好和你的文章完全一致，这种情况也并非不可能出现，但是非常非常困难。
'''
摘要算法应用

摘要算法能应用到什么地方？举个常用例子：

任何允许用户登录的网站都会存储用户登录的用户名和口令。如何存储用户名和口令呢？方法是存到数据库表中：

name    | password
--------+----------
michael | 123456
bob     | abc999
alice   | alice2008

如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。此外，网站运维人员是可以访问数据库的，也就是能获取到所有用户的口令。

正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5：

username | password
---------+---------------------------------
michael  | e10adc3949ba59abbe56e057f20f883e
bob      | 878ef96e86145580c38c87f0410ad153
alice    | 99b1c2188db85afee403b1536010c2c9

当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，如果不一致，口令肯定错误。'''
