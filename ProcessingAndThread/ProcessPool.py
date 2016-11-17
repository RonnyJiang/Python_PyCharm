#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: process pool 进程池。如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
        也是要用到之前的跨平台进程模块multiprocessing
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/17.16:11
"""
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run task %s (%s)...' % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s run %0.2f seconds.' % (name,end-start))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(6):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


'''
可以看出总共开了四个子进程来处理，这个池就4个进程，谁先处理完，就接着处理接下来的任务
请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行
Parent process 4836.
Waiting for all subprocesses done...
Run task 0 (5488)...
Run task 1 (2072)...
Run task 2 (4492)...
Run task 3 (4460)...
Task 1 run 0.49 seconds.
Run task 4 (2072)...
Task 3 run 2.23 seconds.
Run task 5 (4460)...
Task 2 run 2.45 seconds.
Task 4 run 1.99 seconds.
Task 0 run 2.55 seconds.
Task 5 run 0.61 seconds.
All subprocesses done.

'''

