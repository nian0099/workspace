# -*- coding:utf-8 -*-

import requests
import json
import unittest
import HTMLTestRunner
import time

class BaiduFanyiAPi(unittest.TestCase):
    def setUp(self):
        url = "http://fanyi.baidu.com/v2transapi"

    def test_start(self):
        # query = input()
        params = {
            "from":"en",
            "to":"zh",
            "query": "study"
        }
        url = "http://fanyi.baidu.com/v2transapi"
        result = requests.request("post",url, params = params)
        result = json.loads(result.text)
        cutResult = result["liju_result"]["tag"]
        assert (u"学习" in result["liju_result"]["tag"])
        print (cutResult)

    def tearDown(self):
        pass
        

# #接口的url
# url = "http://fanyi.baidu.com/v2transapi"
# #接口的参数
# params = {
#     "from":"en",
#     "to":"zh",
#     "query":"study"
# }
#
# results = requests.request("post",url,params = params)
# #打印返回的结果
# # print(results.text)
#
# #截取需要的字符
# d = json.loads(results.text)
#
# print(d["liju_result"]["tag"])

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    report_name = r"/Users/yoyo/Desktop/other/python3_api/weather_api/report/report"+now+".html"
    re_open = open(report_name,"wb")
    suite = unittest.TestLoader().loadTestsFromTestCase(BaiduFanyiAPi)
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = re_open,
        verbosity = 2,
        title = "百度翻译测试报告",
        description = "百度翻译接口测试详情"

    )
    runner.run(suite)
    re_open.close()
