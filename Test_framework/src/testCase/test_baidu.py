# -*- coding:utf-8 -*-

import os
import sys

# print(sys.path)

os.chdir("/Users/wangxiaonian/Desktop/study/workspace/Test_Framework/")
#打印出项目路径下的目录
for file in os.listdir(os.getcwd()):
    a = file
sys.path.append("/Users/wangxiaonian/Desktop/study/workspace/Test_Framework/")

import time
import unittest
from src.utils.config import Config,DRIVER_PATH,DATA_PATH,REPORT_PATH
from src.utils.log import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.utils.file_reader import ExcelReader
from src.utils.HTMLTestRunner import HTMLTestRunner
from src.utils.mail import Email

class Test_Baidu(unittest.TestCase):
    # 设置url
    URL = Config().get('URL')
    # 打印出项目路径
    # print(URL,DRIVER_PATH)

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
            #subTest意义在于将一个用例根据excel里的数据拆分成n个子用例来执行
                self.sub_setUp()
                self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()

if __name__ == '__main__':
    report = REPORT_PATH + '//report.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='搭建测试框架',description='每日HTML报告')
        runner.run(Test_Baidu('test_search'))
    e = Email(title= "百度搜索测试报告",
              message= "今日测试报告，请查收",
              receiver= "nian110nian@qq.com",
              server= "smtp.163.com",
              sender= "niannian0099@163.com",
              password= "xxn123",#第三方登录客户端时使用授权码登录
              path= report
              )

    # e.send()