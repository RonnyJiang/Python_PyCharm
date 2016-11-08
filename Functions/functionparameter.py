#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:讨论可变参数，关键字参数，命名关键字参数，参数组合
 @author: Ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/8.8:55
"""
# 可变参数
# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
# 我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
# 要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2,3))
# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
nums = [1, 2, 3, 4]
print(calc(nums[0], nums[1], nums[2]))

# 这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
print(calc(*nums))
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
# 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
print(person('Michael', 30))   ##echo: name: Michael age: 30 other: {}
# 也可以传入任意个数的关键字参数：
print(person('Bob', 35, city='Beijing'))
#echo : name: Bob age: 35 other: {'city': 'Beijing'}
print(person('Adam', 45, gender='M', job='Engineer'))
#echo :name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
# 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，
# 其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, city=extra['city'], job=extra['job']))
# echo :name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
#当然，上面复杂的调用可以用简化的写法：
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, **extra))
#echo :name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
##**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
# 仍以person()函数为例，我们希望检查是否有city和job参数：
def person1(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
# 但是调用者仍可以传入不受限制的关键字参数：
print(person1('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456))


"""如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下："""
def person2(name, age, *, city, job):
    print(name, age, city, job)
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# 调用方式如下：
print(person2('Jack', 24, city='Beijing', job='Engineer'))
# Jack 24 Beijing Engineer
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
# >>> person('Jack', 24, 'Beijing', 'Engineer')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: person() takes 2 positional arguments but 4 were given
# 由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。
# 命名关键字参数可以有缺省值，从而简化调用：
def person4(name, age, *, city='Beijing', job):
    print(name, age, city, job)
# 由于命名关键字参数city具有默认值，调用时，可不传入city参数：
print(person4('Jack', 24, job='Engineer'))
# Jack 24 Beijing Engineer
# echo:使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*,Python解释器将无法识别位置参数和命名关键字参数：
# def person(name, age, city, job):
#     # 缺少 *，city和job被视为位置参数
#     pass

"""
小结
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
要注意定义可变参数和关键字参数的语法：
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
以及调用函数时如何传入可变参数和关键字参数的语法：
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
"""