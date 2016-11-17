#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: 多进程，这个在linux用os模块的fork方法
        由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/17.14:43
"""
# 要让Python程序实现多进程（multiprocessing），我们先了解操作系统的相关知识。
#
# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
# 因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
#
# 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，
# 而子进程只需要调用getppid()就可以拿到父进程的ID。
#
# Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：

# 在linux内核中可以运行fork接口来创建一个子进程，但在windows下没有这个接口，先看一下只有在linux或max下能运行的创建进程的例子
'''此块在Unix/Linux/Max运行，windows下注释掉了'''
# import os
#
# print('Process (%s) start.....' % os.getpid())
# #only works on Unix/Linux/Max
# pid = os.fork()
# if pid == 0:
#     print('I am Child process(%s) and my parent is %s.' % (os.getpid(),os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(),pid))
'''
直接运行没问题，但是单步调试报错python -m pdb myMultiProcessing.py，以后再论吧
ronny@ronny:~/shareDoc/pycharm$ python myMultiProcessing.py
Process (8244) start.....
I (8244) just created a child process (8245).
I am Child process(8245) and my parent is 8244.
由于Windows没有fork调用，上面的代码在Windows上无法运行。由于Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行是没有问题的

有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，
就fork出子进程来处理新的http请求。
'''

# 如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows没有fork调用，难道在Windows上无法用Python编写多进程的程序？
#
# 由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
#
# multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
from multiprocessing import Process    ##之前脚本名跟模块同名了，所以本来正常该有的不见了，所切忌不要和系统的module重名
import os

#子进程要执行的代码
def run_proc(name):
    print('I am child process %s(%s)' % (name,os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('Child process will start!')
    p.start()
    # print('child process id = %s' % p.pid)   ##p.start--p.join之间最好不要加任何语句
    p.join()
    print('Child process end!')

'''
echo:
Parent process 4772.
Child process will start!
# child process id = 5364
I am child process test(5364)
Child process end!
'''
# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。


