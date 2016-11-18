#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: 当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。

        获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放。
        锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上
        只能以单线程模式执行，效率就大大地下降了。其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，
        导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/18.11:10
"""

# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，
# 所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
#
# 来看看多个线程同时操作一个变量怎么把内容给改乱了：

import threading,time,random

#假定这是你的银行存款
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0
    global balance

    balance = balance + n
    x = balance = balance - n
    if x != 0:
        print(x)


def run_thread(n):
    for i in range(1000000):   #如果不加锁，在range（一百万时，就会有上万个不为0的值），
        lock.acquire()     #加锁
        try:
            change_it(n)
        finally:
            lock.release()    #解锁
            pass
t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()

t1.join()
t2.join()


'''
如下一大堆废话要说的就是：这个加减赋值的语句不是原子操作！！！
原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：

balance = balance + n

也分两步：

    计算balance + n，存入临时变量中；
    将临时变量的值赋给balance。

也就是可以看成：

x = balance + n
balance = x

究其原因，是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了。

两个线程同时一存一取，就可能导致余额不对，你肯定不希望你的银行存款莫名其妙地变成了负数，
所以，我们必须确保一个线程在修改balance的时候，别的线程一定不能改。

如果我们要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，
因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，
同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现：
'''
