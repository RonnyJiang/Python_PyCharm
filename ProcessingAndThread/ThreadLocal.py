#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写自身线程加入的属性，但互不影响。
        一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
        ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
        用它我们可以做签名，创建目录，然后每个线程各自做自己的签名，拷到各自对应的目录
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/18.16:04
"""

import threading
import logging,os
# 创建全局ThreadLocal对象:
local_directory = threading.local()

stra = 'abcdefg.apk'
print(os.path.split(stra))     ###获取路径和后缀
print(os.path.splitext(stra))
def handle_signature():
    handle_dir = local_directory.dir
    unsignedApp = local_directory.file
    signed_app = ''
    print('hello I will handle')
    if str(unsignedApp).lower().endswith('.apk'):
        signed_app = str(unsignedApp).replace(".","_signed.")

    elif str(unsignedApp).lower().endswith('.pkg'):
        signed_app = str(unsignedApp).replace(".pkg","_signed.pkg")
    else:
        logging.error('ErrorType: not app or pkg')
    print('signature app: %s to %s' % (unsignedApp, signed_app))
    print('%s sginature success...!>>>signed package %s will save in %s' % (threading.current_thread().name,signed_app,handle_dir))

def signature_thread(des_dir,unsign_file):
    local_directory.dir = des_dir
    local_directory.file = unsign_file
    handle_signature()

t1 = threading.Thread(target=signature_thread,args=('/home/ronny/dir1','LtMarke.t.Apk',),name = 'thread-t1')
t2 = threading.Thread(target=signature_thread,args=('/home/ronny/dir2','contacts.pkg',),name = 'thread-t2')
t1.start()
t2.start()
t1.join()
t2.join()
'''
小结
一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
'''
