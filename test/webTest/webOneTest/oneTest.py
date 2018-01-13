#coding:utf-8

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class  KeySearch(unittest.TestCase):
    def setUp(self):
        print("start to test")
        self.browser = webdriver.Safari()

    def test_search_in_Baidu(self):
        browser = self.browser
        browser.get('http://www.baidu.com')
        self.assertIn("百度", browser.title)
        elem = browser.find_element_by_id("kw")
        elem.send_keys("test")
        if browser.find_elements_by_id("su"):
            for i in  range(5):
                print('111')
            # for elem in 20:
            #     elem = browser.find_elements_by_id('su').click()
        else:
            print('222')
        elem.send_keys(Keys.RETURN)
        #self.assertIn("结果",browser.page_source)  # 有点问题， 待调试



    def tearDown(self):
        print("tearDown the test")
        time.sleep(5)
        self.browser.close()

if __name__ == "__main__":
    unittest.main()