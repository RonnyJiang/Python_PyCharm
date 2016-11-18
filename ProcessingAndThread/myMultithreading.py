#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: 多线程，多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
        Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
        由于GIL的存在，CPU计算任务多线程性能无法提升，但是如果是网络IO如爬网，或磁盘IO操作，用多线程还是可以提升效率的。
        因为IO操作不锁定GIL，这时其他线程可以正常执行
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/18.10:20
"""

# 我们前面提到了进程是由若干线程组成的，一个进程至少有一个线程。
#
# 由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，
# 而不是模拟出来的线程。
#
# Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，
# 我们只需要使用threading这个高级模块。
#
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
import threading,time
# n = 0
def loop():
    print('Thread %s is running...' % threading.current_thread().name)
    n = 0
    # global n    如果n是在全局定义的，就要用global 定义
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(2)
    print('Thread %s ended...' % threading.current_thread().name)

t = threading.Thread(target=loop,name='LoopThread')
t.start()
print('----continue exec main thread----')
t.join()
print('thread %s ended.' % threading.current_thread().name)

'''
输出结果如下： 可以看到执行子线程时，主线程也一直在继续往下执行。打印----continue exec main thread----后才在t.join上等子线程结束
Thread LoopThread is running...
thread LoopThread >>> 1
----continue exec main thread----
thread LoopThread >>> 2
thread LoopThread >>> 3
thread LoopThread >>> 4
thread LoopThread >>> 5
Thread LoopThread ended...
thread MainThread ended.

由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，
它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。名字仅仅在打印时用来显示，
完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……

'''
