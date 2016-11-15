#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: 错误处理,抛异常   try...except...finally...
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/15.16:08
"""

# 在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。在操作系统提供的调用中，
# 返回错误码非常常见。比如打开文件的函数open()，成功时返回文件描述符（就是一个整数），出错时返回-1。
#
# 用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起，造成调用者必须用大量的代码来判断是否出错：
#
# def foo():
#     r = some_function()
#     if r==(-1):
#         return (-1)
#     do something
#     return r
#
# def bar():
#     r = foo()
#     if r==(-1):
#         print('Error')
#     else:
#         pass
#
# 一旦出错，还要一级一级上报，直到某个函数可以处理该错误（比如，给用户输出一个错误信息）。
#
# 所以高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。
'''让我们用一个例子来看看try的机制：'''
try:
    print('try...ronny...')
    r = 10/0
    print('result:' ,r)
except ZeroDivisionError as e:
    print('except: ',e)
finally:
    print('finally...ronny...')
print('END')

'''
输出：
try...ronny..
except:  division by zero
finally...
END
当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。

从输出可以看到，当错误发生时，后续语句print('result:', r)不会被执行，except由于捕获到ZeroDivisionError，因此被执行。
最后，finally语句被执行。然后，程序继续按照流程往下走。

如果把除数0改成2，则执行结果如下：
'''

try:
    print('try...ronny...')
    r = 10/2
    print('result:' ,r)
except ZeroDivisionError as e:
    print('except: ',e)
finally:
    print('finally...ronny...')
print('END')

# 由于没有错误发生，所以except语句块不会被执行，但是finally如果有，则一定会被执行（可以没有finally语句）。
#
# 你还可以猜测，错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理。没错，可以有多个except来捕获不同类型的错误：

try:
    print('try...ronny...')
    # print(int('a',base=16))
    r = 10/ int('a')  #r = 10/ int('a',base=16)  then OK! default base = 10
    print('resulta:',r)
except ValueError as e:
    print('valueError:',e)    ##echo: valueError: invalid literal for int() with base 10: 'a'
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
finally:
    print('finally ...ronny...')
print('END')

# int()函数可能会抛出ValueError，所以我们用一个except捕获ValueError，用另一个except捕获ZeroDivisionError。
#
# 此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

# Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，
# 它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：
# def foo():
#     pass
#
# try:
#     foo()
# except ValueError as e:
#     print('ValueError')
# except UnicodeError as e:
#     print('UnicodeError')

''' 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。'''
#
# Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
#
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
#
# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，
# 这时，只要main()捕获到了，就可以处理：

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        print('start error check')
        bar('0')
    except Exception as e:   #echo : Exception 是比较高的父类，一版不确定是什么错时，可以抛Exception错
        print('Error:', e)
    finally:
        print('finally...')
        print('end error check')
main()
# 也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。这样一来，就大大减少了写try...except...finally的麻烦。
