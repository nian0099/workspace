# -*- coding:utf-8 -*-

import os
import time
import unittest
from src.utils.config import Config,DRIVER_PATH,DATA_PATH
from src.utils.log import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.utils.file_reader import ExcelReader

class Test_Baidu(unittest.TestCase):
    # 设置url
    URL = Config().get('URL')
    print(URL,DRIVER_PATH)

    excel = DATA_PATH + '/baidu.xlsx'

    locator_kw = (By.ID, "kw")

    locator_su = (By.ID, "su")

    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def sub_setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + "/chromedriver")
        self.driver.get(self.URL)

    def sub_tearDown(self):
        self.driver.quit()

    # def test_SearchBaidu01(self):
    #     self.driver.find_element(*self.locator_kw).send_keys('selenium 灰蓝')
    #     self.driver.find_element(*self.locator_su).click()
    #     time.sleep(2)
    #     links = self.driver.find_elements(*self.locator_result)
    #     for link in links:
    #         logger.info(link.text)
    #
    # def test_SearchBaidu02(self):
    #     self.driver.find_element(*self.locator_kw).send_keys('Python Selenium')
    #     self.driver.find_element(*self.locator_su).click()
    #     time.sleep(2)
    #     links = self.driver.find_elements(*self.locator_result)
    #     for link in links:
    #         logger.info(link.text)

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()

if __name__ == '__main__':
    unittest.main()