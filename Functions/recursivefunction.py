#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: recursive function(递归函数)
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/8.10:23
"""

# 我们来计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示，可以看出：
#
# fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
# 上面就是一个递归函数。可以试试：
print(fact(3))
print(fact(8))


"""
使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
可以试试fact(100),fact(1000)
"""
print(fact(100))    #超级大的数
print(fact(200))    ##没见过这么大的数
#print(fact(1000))   ##栈溢出 报错RecursionError: maximum recursion depth exceeded in comparison，超过了最大的默认递归深度


###用尾递归
"""
尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。
要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：
"""
def factend(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1,num*product)

#调用尾递归
print(factend(8))

"""
---------------------------------------------------------------------------------------------------------
小结

使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
----------------------------------------------------------------------------------------------------------
"""


###练习：：用递归写个汉诺塔