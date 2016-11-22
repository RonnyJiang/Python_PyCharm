#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc: GUI EG, LABEL AND BUTTON
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/22.12:46
"""

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()   #创建个对话框

    def createWidgets(self):
        self.hellolabel = Label(self, text='Hello,WORLD')   #在对话框中创建一个label
        self.hellolabel.pack()
        self.editlabel = Entry(self, text = 'please input')   #在对话框中创建一个editcontrol
        self.editlabel.pack()
        self.helloButton = Button(self, text='hello', command=self.hello)  #在对话窗创建一个button，并让其响应hello事件
        self.helloButton.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)  #在对话窗创建一个button，并让其响应quit事件
        self.quitButton.pack()
    def hello(self):
        name = self.editlabel.get() or 'ronny'
        messagebox._show(title='Hi HY',message='hello %s' % name)
# 在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
#
# pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
#
# 在createWidgets()方法中，我们创建一个Label和一个Button，当Button被点击时，触发self.quit()使程序退出。
#
# 第三步，实例化Application，并启动消息循环：
app = Application()
# 设置窗口标题:
app.master.title("hello ronny")
# # 主消息循环:
app.mainloop()

