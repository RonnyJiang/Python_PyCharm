#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: pdb---Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/16.10:41
"""
'''
s = '0'
n = int(s)
print(10/n)
'''


# C:\python_project\Python_PyCharm\Pdb_Debug>python -m pdb pdb_debug.py
# 以参数-m pdb启动后，pdb定位到下一步要执行的代码"""
# > c:\python_project\python_pycharm\pdb_debug\pdb_debug.py(9)<module>()
# -> """
# (Pdb) n   -> s = '0'。输入命令n可以单步执行代码：输入命令l来查看代码：
# (Pdb) l
#   4      @desc: pdb---Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。
#   5      @author: ronny
#   6      @contact: set@aliyun.com
#   7      @site: www.lemon.pub
#   8      @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/16.10:41
#   9  -> """
#  10
#  11     s = '0'
#  12     n = int(s)
#  13     print(10/n)
#  14

# > c:\python_project\python_pycharm\pdb_debug\pdb_debug.py(11)<module>()
# -> s = '0'   #输入命令n可以单步执行代码
# (Pdb) n
# > c:\python_project\python_pycharm\pdb_debug\pdb_debug.py(12)<module>()
# -> n = int(s)
# (Pdb) n  #输入命令n可以单步执行代码
# > c:\python_project\python_pycharm\pdb_debug\pdb_debug.py(13)<module>()
# -> print(10/n)
# (Pdb) p s     #任何时候都可以输入命令p 变量名来查看变量：
# '0'
# (Pdb) p n     #任何时候都可以输入命令p 变量名来查看变量：
# 0
# (Pdb) n       #输入命令n可以单步执行代码
# ZeroDivisionError: division by zero
# > c:\python_project\python_pycharm\pdb_debug\pdb_debug.py(13)<module>()
# -> print(10/n)
# (Pdb) q

# 这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，如果有一千行代码，要运行到第999行得敲多少命令啊。还好，我们还有另一种调试方法
import pdb

s = '0'
n = int(s)
pdb.set_trace()    # 运行到这里会自动暂停,且IDE直接可以运行，然后直接运行到这输入n 即可
print(10/n)

# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：
# > c:\python_project\python_pycharm\pdb_debug\pdb_debug.py(59)<module>()
# -> print(10/n)
# (Pdb) n
# ZeroDivisionError: division by zero
# > c:\python_project\python_pycharm\pdb_debug\pdb_debug.py(59)<module>()
# -> print(10/n)
# (Pdb) p n         #命令p查看变量
# 0
# (Pdb) p s
# '0'
# (Pdb) c          #命令c继续运行：
# Traceback (most recent call last):
#   File "C:/python_project/Python_PyCharm/Pdb_Debug/pdb_debug.py", line 59, in <module>
#     print(10/n)
# ZeroDivisionError: division by zero
#

'''
小结

写程序最痛苦的事情莫过于调试，程序往往会以你意想不到的流程来运行，你期待执行的语句其实根本没有执行，这时候，就需要调试了。

虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。
'''