#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2

# 方法一:构建一个HTTPHandler处理器对象，支持处理HTTP的请求
#http_handler = urllib2.HTTPHandler()

# 方法二:在HTTPHandler增加参数"debuglevel=1"将会自动打开Debug log 模式，
# 程序在执行的时候会打印收发包的信息
http_handler = urllib2.HTTPHandler(debuglevel=1)

# 调用build_opener()方法构建一个自定义的opener对象，参数是构建的处理器对象
opener = urllib2.build_opener(http_handler)

request = urllib2.Request("http://www.baidu.com/")

# 调用自定义opener对象的open()方法，发送request请求
response = opener.open(request)

print response.read()

