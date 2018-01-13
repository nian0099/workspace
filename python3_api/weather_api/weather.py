# -*- coding:utf-8 -*-

import json
import requests
import unittest

class weatherApiTest(unittest.TestCase):
    def setUp(self):
        print("start")

    def test_weatherApi(self):
        url = "http://wthrcdn.etouch.cn/weather_mini"

        params = {
            "city":"北京"
        }

        result = requests.get(url,params = params)
        result = json.loads(result.text)
        cutresult = result["data"]["forecast"][0]["type"]
        print(cutresult)
        if (cutresult == "晴"):
            print("验证通过")
        else:
            print("验证失败")

    def tearDown(self):

        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)

# result = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=北京")
#
#
#
# print (result.text,u'\n数据类型:',type(result.text))
#
# #对数据进行反序列化操作
# dic = json.loads(result.text)
#
# print (dic,u'\n数据类型:',type(dic))
