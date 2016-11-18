#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:获取路径+文件名， 和获取文件名+文件扩展名
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/18.17:29
"""

# 本文实例讲述了python根据给定文件返回文件名和扩展名的方法。分享给大家供大家参考。具体分析如下：
#
# 这段代码可以根据文件的完整路径返回文件名和扩展名，python的函数可以同时返回两个值，用起来就更方便了


def GetFileNameAndExt(filename):
    import os
    (filepath, tempfilename) = os.path.split(filename);
    (shotname, extension) = os.path.splitext(tempfilename);
    print(filepath,tempfilename,shotname,extension)
    return shotname, extension

print(GetFileNameAndExt('/home/ronny/app_sign/Ltmarket.apk'))