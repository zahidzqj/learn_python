 #!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
#import urllib2
from urllib2 import Request
from urllib2 import urlopen
url = "http://www.baidu.com/s"
headers = {"User-Agent" : "Mozilla 。。。。"}

keyword = input("张请输入需要查询的关键字： ")

wd = {"wd" : keyword}

# 通过urllib.urlencode() 参数是一个dict类型
wd = urllib .urlencode(wd)

# 拼接完整的url
fullurl = url + "?" + wd

# 构造请求对象
request = Request(fullurl, headers = headers)

response = urlopen(request)

print (response.read())
