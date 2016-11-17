#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: 进程间通信  Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换进程间数据。
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/17.17:56
"""

# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
# Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
#
# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
from multiprocessing import Process,Queue
import os,time,random

# 写数据进程执行的代码:
def wirte(q):
    print('process to write %s' % os.getpid())
    for value in ['A','B','C']:
        time.sleep(10)
        print('put %s to Queue ....' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=wirte,args=(q,))
    pr = Process(target=read,args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

'''
echo:
process to write 3800
Process to read 5600
put A to Queue ....
Get A from queue.
put B to Queue ....
Get B from queue.
put C to Queue ....
Get C from queue.
'''

'''
------------------------------------------------------------------
小结

在Unix/Linux下，可以使用fork()调用实现多进程。

要实现跨平台的多进程，可以使用multiprocessing模块。

进程间通信是通过Queue、Pipes等实现的。
------------------------------------------------------------------
'''
