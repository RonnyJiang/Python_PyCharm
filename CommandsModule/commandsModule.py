#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: commands 模块.Python中的commands模块专门用于调用Linux shell命令，并返回状态和结果
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/11.18:41
"""
import commands
# 用Python写运维脚本时，经常需要执行linux shell的命令，这就需要用到commands模块
# 下面是commands模块的3个主要函数：

# 1. commands.getoutput('shell command')
# 执行shell命令，返回结果（string类型）
commands.getoutput('pwd')   #echo :'/home/ronny'

# 2. commands.getstatus('file')
# 该函数已被python丢弃，不建议使用,目前可以用，它返回 ls -ld file 的结果（String）(返回结果太奇怪了，难怪被丢弃）
commands.getstatus('addon.zip')
# echo : '-rw-rw-r-- 1 ronny ronny 873751 10\xe6\x9c\x88 19 11:09 addon.zip'

# 3. commands.getstatusoutput('shell command')
# 执行shell命令, 返回两个元素的元组tuple(status, result)，status为int类型，result为string类型。#
# cmd的执行方式是{ cmd ; } 2>&1, 故返回结果包含标准输出和标准错误.
commands.getstatusoutput('pwd') #echo :(0, '/home/ronny')
