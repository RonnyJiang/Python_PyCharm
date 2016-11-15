#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: 调用堆栈。如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/15.16:58
"""
def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2

def main():
    bar('0')

main()




'''
Traceback (most recent call last):
  File "C:/python_project/Python_PyCharm/ErrorHanding/callStack/callStack.py", line 19, in <module>
    main()
    调用main()出错了,但原因是第17行

  File "C:/python_project/Python_PyCharm/ErrorHanding/callStack/callStack.py", line 17, in main
    bar('0')
    调用bar('0')出错了,但原因是第14行
  File "C:/python_project/Python_PyCharm/ErrorHanding/callStack/callStack.py", line 14, in bar
    return foo(s)*2
    调用oo(s)出错了,但原因是第11行
  File "C:/python_project/Python_PyCharm/ErrorHanding/callStack/callStack.py", line 11, in foo
    return 10/int(s)
ZeroDivisionError: division by zero
原因是return 10 / int(s)这个语句出错了，这是错误产生的源头，因为下面打印了：
第11行 error,原因 ZeroDivisionError: division by zero
根据错误类型ZeroDivisionError，我们判断，int(s)本身并没有出错，但是int(s)返回0，在计算10 / 0时出错，至此，找到错误源头。
'''

