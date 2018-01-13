# -*- coding: utf-8 -*-

import ssl
from urllib import request

ssl._create_default_https_context = ssl._create_unverified_context
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('status: ',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s: %s' % (k,v))
print('data: ',data.decode('utf-8'))


# import ssl
# from urllib import request
#
#
# ssl._create_default_https_context = ssl._create_unverified_context
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))
