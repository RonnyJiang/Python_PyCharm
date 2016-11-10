#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: logging 模块
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/10.15:55
"""

import logging
def getmylog():
    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warn message')
    logging.error('error message')
    logging.critical('critical message')

# getmylog()
# 输出：
#
#     WARNING:root:warn message
#     ERROR:root:error message
#     CRITICAL:root:critical message


'''
默认情况下，logging模块将日志打印到屏幕上(stdout)，日志级别为WARNING(即只有日志级别高于WARNING的日志信息才会输出)
日志格式如---》所示：WARNING  : root          :  warn message
          分别对应：日志级别  ： Logger实例名称 ： 日志消息内容

问题来了:
        日志级别等级及设置是怎样的？
        怎样设置日志的输出方式？比如输出到日志文件中？
日志级别
级别 	何时使用
DEBUG 	详细信息，典型地调试问题时会感兴趣。
INFO 	证明事情按预期工作。
WARNING 	表明发生了一些意外，或者不久的将来会发生问题（如‘磁盘满了’）。软件还是在正常工作。
ERROR 	由于更严重的问题，软件已不能执行一些功能了。
CRITICAL 	严重错误，表明软件已不能继续运行了。

'''

# 通过下面的方式进行简单配置输出方式与日志级别
# logging.basicConfig(filename='logger.log', level=logging.INFO)
logging.basicConfig(filename='ronny.log',level=logging.DEBUG)   ##这样就会创建一个ronny.log，把输出写到ronny.log

getmylog()

# 问题又来了
#
#         通过上述配置方法都可以配置那些信息？
#
# 在解决以上问题之前，需要先了解几个比较重要的概念，Logger，Handler，Formatter，Filter
'''
几个重要的概念

    Logger 记录器，暴露了应用程序代码能直接使用的接口。
    Handler 处理器，将（记录器产生的）日志记录发送至合适的目的地。
    Filter 过滤器，提供了更好的粒度控制，它可以决定输出哪些日志记录。
    Formatter 格式化器，指明了最终输出中日志记录的布局。
'''




