# codeing: utf-8

from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from HTMLTestRunner  import HTMLTestRunner

class KeySearch(unittest.TestCase):
    '搜索测试'
    def setUp(self):
        print('start test')
        self.browser = webdriver.Safari()

    def test_Search_in_Baidu(self):
        print('search in baidu')
        browser = self.browser
        browser.get('http://www.baidu.com')
        self.assertIn("百度",browser.title)
        elem = browser.find_element_by_id('kw')
        elem.send_keys('test')
        elem.send_keys(Keys.RETURN)
        self.assertIn("结果",browser.page_source)
        # print("%s",browser.page_source)

    # def test_Search_in_Google(self):
    #     print("search in google")
    #     browser = self.browser
    #     browser.get("https://www.google.co")
    #     self.assertIn("Google",browser.title)
    #     elem = browser.find_element_by_id('lst-ib')
    #     elem.send_keys("test")
    #     elem.send_keys(Keys.RETURN)
        #self.assertIn("result:",browser.page_source)

    def tearDown(self):
        print('tearDown the test')
        time.sleep(5)
        self.browser.close()

testunit = unittest.TestSuite()
testunit.addTest(KeySearch("test_Search_in_Baidu"))
fp = open('./result.html', 'wb')
runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试执行情况')
runner.run(testunit)
fp.close()

if __name__ == "__main__":
    unittest.main()

