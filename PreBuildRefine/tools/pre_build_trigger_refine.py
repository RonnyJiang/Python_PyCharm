#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/10.14:58
"""
import os
import logging
'''
几个重要的概念

    Logger 记录器，暴露了应用程序代码能直接使用的接口。
    Handler 处理器，将（记录器产生的）日志记录发送至合适的目的地。
    Filter 过滤器，提供了更好的粒度控制，它可以决定输出哪些日志记录。
    Formatter 格式化器，指明了最终输出中日志记录的布局。
'''
def GetLog():
    """Initialize the global log"""

    logger = logging.getLogger(__name__)   #创建记录器
    console = logging.StreamHandler()    #创建处理器
    formatter = logging.Formatter('%(asctime)s %(levelname)s(%(thread)d)    \
            : %(message)s')        #创建格式化器
    #  %(asctime)s 	打印日志的时间
    # %(levelname)s 打印日志级别名称
    # %(thread)d 	打印线程id
    # %(message)s 	打印日志信息

    logger.addHandler(console)     #为记录器增加处理器
    console.setFormatter(formatter)   #设置一个格式化器formatter
    file = logging.FileHandler(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pre_build_trigger.log'))
    # logger.warning('warn message')
    # logger.setLevel(logging.INFO)     #设置日志级别
    '''当单独运行pre_build_trigger_refine.py时print(__name__)显示为__main__,
       当其他py调用这个py中的GetLog方法时:
       from pre_build_trigger_refine import GetLog

       GetLog()
       __name__显示为pre_build_trigger_refine

    '''
    print(logger)
    print(__name__)
    # logger = logging.getLogger(__name__)
    # console = logging.StreamHandler()
    # formatter = logging.Formatter('%(asctime)s %(levelname)s(%(thread)d)    \
    #         : %(message)s')
    # console.setFormatter(formatter)
    # logger.addHandler(console)
    #
    # file = logging.FileHandler(
    #     os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pre_build_trigger.log'))
    # file.setFormatter(formatter)
    # logger.addHandler(file)
    # logger.setLevel(logging.INFO)
    # return logger


def main():
    GetLog()




if __name__ == '__main__':
    main()
