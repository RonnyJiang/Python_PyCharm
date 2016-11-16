### Python_PyCharm  主要存放python学习demo
##### Author ： RonnyJiang


* 感言：
之前学习都很零散，一段时间不学就忘记了，编写过的代码也没有系统管理过。
删的删，没的没。现在要把所学的python内容都系统的归纳到这个项目。看明年的自己python是不是会了。

有志者事竟成，破釜沉舟，百二秦关终属楚；
苦心人天不负，卧薪尝胆，三千越甲可吞吴。


**以大多数人的努力程度之低，根本轮不到拼天赋**


                                                          --2016.10.31
                                                                     
--------------------------------------------------------------------------------------------------
###列表：

####基础
* HelloWorld     --python输入输出，以及设置file模板  
* StringCoding   --python的字符串与编码
* ListAndTuple   --python列表和元组
* JudgeAndLoop   --if判断及for.while循环
* DictAndSet     --字典和集合
* Functions      --函数，内建函数，自定义函数，函数参数，函数参数类型校验，多个返回值，递归函数

####高级特性
在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。
基于这一思想，就需要学习掌握Python中非常有用的高级特性，1行代码能实现的功能，决不写5行代码。
请始终牢记，代码越少，开发效率越高。
* Slice          --切片，可以对list tuple 常量字符串等快速遍历截取其中的数据片段
* Iteration      --迭代，任何可迭代对象都可以作用于for循环，进行迭代
* ListComprehensions --列表生成式，生成复杂的列表，not eg:list(range(10))
* 生成器和迭代器略

####函数式编程
* 高阶函数         --一个函数接收另一个函数作为参数，这种函数就称之为高阶函数。
* MapReduce       --Python内建了map()和reduce()函数,利用mapreduce实现str2int和str2float函数
* Sort            ——Sort也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
* Lambda          --匿名函数，Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数
* PartialFunction --偏函数，方便在原有函数基础上，固定个别参数，生成新的函数，eg int函数固定base

####模块
* 模块说明         --模块说明，又引入了按目录来组织模块的方法，称为包（Package），及__init__.py说明
* HelloModule     --创建模块
* HelloModuleTest --使用测试刚刚创建的模块
* InstallAndUseModule  --安装pip，并通过pip安装第三方库—Python Imaging Library--PIL，然后制作缩略图

####面向对象编程
* ObjectDemo      --创建一个class，分析面向对象编程的设计思想及与面向过程的区别
* ClassAndInstance--类和实例 面向对象最重要的概念就是类（Class）和实例（Instance）
* PrivateProtect  --访问限制,将类中不想被访问的变量限制访问，实际上限制总有办法访问
* InheritanceAndPolymorphism  --继承和多态

####面向对象高级编程
【数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。在Python中，面向对象还有很多高级特性，允许我们写出非常强大的功能。
我们会讨论多重继承、定制类、元类等概念】
* __slots__      --限制类被绑定的属性，防止随意绑定属性
* property       使用@property装饰器负责把一个方法变成属性调用

####错误、调试和测试
* ErrorHanding     --错误处理(try...except...finally),调用堆栈、记录错误（logging）、抛出错误（raise）
* debug            --调试（pdb，IDE,logging)--虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。

####IO 编程
* IOStream/ReasWriteFile --文件读写  还介绍了with ..as..用以解决open异常，f.close的case