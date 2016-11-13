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
import commands
'''
几个重要的概念

    Logger 记录器，暴露了应用程序代码能直接使用的接口。
    Handler 处理器，将（记录器产生的）日志记录发送至合适的目的地。
    Filter 过滤器，提供了更好的粒度控制，它可以决定输出哪些日志记录。
    Formatter 格式化器，指明了最终输出中日志记录的布局。
'''

def GetLog():
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
    file.setFormatter(formatter)
    logger.addHandler(file)
    logger.setLevel(logging.INFO)

    logger.setLevel(logging.INFO)     #设置日志级别
    #当单独运行pre_build_trigger_refine.py时print(__name__)显示为__main__,
    # 当其他py调用这个py中的GetLog方法时:
    # from pre_build_trigger_refine import GetLog
    #
    # GetLog()
    # __name__显示为pre_build_trigger_refine
    return  logger

LOG = GetLog()    ###LOG为我创建的logger对象，以后用这个对象去打印log，在每个函数头尾打印log，以方便定位错误发生在哪个函数

def run_shell_command(cmd):
    sys = os.name
    if sys == 'posix':
        LOG.info(cmd)
        return commands.getstatusoutput(cmd)
    else:
        return 'System of the PC is not a posix'

def get_env(ev):
    return os.environ.get(ev)

def get_profile_list(content):


def get_change_content(gerrit_ip="10.27.254.101", gerrit_port="29000"):
    # change_id = get_env("JAVA_HOME")     ##参数为JAVA_HOME时echo：C:\Program Files\Java\jdk1.7.0_80
    # print(gerrit_ip,gerrit_port,change_id)
    change_id = get_env("GERRIT_CHANGE_ID")
    command = "ssh -p %s %s gerrit query %s --file --current-patch-set" % (gerrit_port,gerrit_ip,change_id)
    status,content = run_shell_command(command)
    if status == 0:
        LOG.info("get_change_content = %s" % content)
        return content
    else:
        LOG.error("get change content error")
        return None


def update_trigger_config():
    LOG.info('update_trigger_config in')
    change_content = get_change_content()

    profile_list = get_profile_list(get_env("profile"))

    LOG.info('update_trigger_config out')


def main():
    LOG.info('main in')

    update_trigger_config()
    # run_shell_command('aa')
    LOG.info('main out')



if __name__ == '__main__':
    main()


