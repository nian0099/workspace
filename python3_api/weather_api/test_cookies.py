# -*- coding:utf-8 -*-

import requests
import urllib.request
import urllib.parse
import http.cookiejar

filename = "cookie.txt"
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = http.cookiejar.MozillaCookieJar(filename)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
post_data = urllib.parse.urlencode({
    "name":"汪利念",
    "password":"123456"
}).encode("utf-8")
#登录公司测试后台
LOGIN_URL = "http://ophwtest.yoyo-corp.com/index.php?s=/Home/Index-login.html"
#模拟登录，并把cookie保存到变量
result = opener.open(LOGIN_URL,post_data)
#保存cookie到cookie文件中
cookie.save(ignore_discard=True,ignore_expires=True)
#利用保存的cookie模拟已经登录的状态下打开首页广告编辑地址
grade_url = "http://ophwtest.yoyo-corp.com/index.php?s=/Sticker2017/Home-edit-id-125.html"
#开始请求
result = opener.open(grade_url)
print(result.read().decode("utf-8"))


