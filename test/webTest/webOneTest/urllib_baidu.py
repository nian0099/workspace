# -*- coding:utf-8 -*-

__author__ = 'Mr.汪'

import urllib.parse
import urllib.request

if __name__ == '__main__':
    print('打印urllib的实例')
    response = urllib.request.urlopen('http://www.baidu.com')

    html = response.read().decode(encoding="utf-8")
    print('print:',html)

    header = response.info()
    print('print::',header)

    status_code = response.getcode()
    print('print:::',status_code)

    url = response.geturl()
    print('print:::;',url)
