# -*- coding:utf-8 -*-

import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_Baidu(unittest.TestCase):
    # 设置url
    URL = "http://www.baidu.com"
    # 设置根文件目录，这里表示的是去掉最后两个路径
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    print(BASE_PATH)
    DRIVER_PATH = os.path.abspath(BASE_PATH + '/drivers/chromedriver')
    print(DRIVER_PATH)

    locator_kw = (By.ID, "kw")
    locator_su = (By.ID, "su")
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=self.DRIVER_PATH)
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_SearchBaidu01(self):
        self.driver.find_element(*self.locator_kw).send_keys('selenium 灰蓝')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)

    def test_SearchBaidu02(self):
        self.driver.find_element(*self.locator_kw).send_keys('Python Selenium')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)

if __name__ == '__main__':
    unittest.main()