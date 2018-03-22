# -*- coding: utf-8 -*-

import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
import time
import HTMLTestRunner

class PhilmIOSTests(unittest.TestCase):

    def setUp(self):

        print u"我要启动app了"

#         app = os.path.abspath('/Users/yoyo/Desktop/other/appium_ios_sample_code-master/apps/HHH/build/Debug-iphoneos/HHH.app')
        self.driver = webdriver.Remote(
                               command_executor='http://127.0.0.1:4723/wd/hub',
                               desired_capabilities={
                               # 'app': app,
                               'platformName': 'iOS',
                               'platformVersion': '11.2',
                               'deviceName': 'Blue',
                               'bundleId': 'com.yoyoshijie.philm',
                               'automationName': 'XCUITest',
                               'udid': '0facfa822a68605fb9cdc23ea7feb8e37cc57cfc',
                               })

    def test_action(self):

        sleep(3)
        print u"等3秒开始测试"

        el1 = self.driver.find_element_by_accessibility_id("艺术滤镜")
        el1.click()
        el2 = self.driver.find_element_by_accessibility_id("照片")
        el2.click()
        el3 = self.driver.find_element_by_accessibility_id(
            "/var/containers/Bundle/Application/D81C4A3A-54DA-4156-BE5E-970B7D413211/Philm.app/images.bundle/item_cover_35638@2x.png")
        el3.click()
        # el4 = self.driver.find_element_by_accessibility_id("Art3")
        # el4.click()
        sleep(3)
        el5 = self.driver.find_element_by_accessibility_id("icon more normal")
        el5.click()
        sleep(3)
        el6 = self.driver.find_element_by_accessibility_id("icon local normal2@2x")
        el6.click()
        sleep(3)
        print u"搞定，收工"
        # if lbbb.text == "appium test succeed" :
        #     self.self.driver.find_element_by_accessibility_id('button').click()
            #
            # bbbb = self.self.driver.find_element_by_accessibility_id("bbbb")
            #
            # sleep(1)
            # lbbb = self.self.driver.find_element_by_class_name("XCUIElementTypeStaticText")
            # textF1 = self.self.driver.find_element_by_name('HHH')
            #
            # print("HHHHHHHH1 %s" % (self.self.driver.contexts))
            # print("HHHHHHHH2 %s" % (self.self.driver.page_source))
            # print("HHHHHHHH3 %s %s" % (lbbb, textF1))
            #
            # textF1.send_keys("HHHHHHH")
            #
            # sleep(1)
            # self.self.driver.hide_keyboard()
            #
            # bbbb.click()
            #
        try:
            sleep(1)
        except:
            pass


    # def tearDown(self):
    #     sleep(5)
    #     print u"搞定，收工"
        self.driver.quit()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PhilmIOSTests)
    unittest.TextTestRunner(verbosity=1).run(suite)
    #
    # timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    # filename = "/Users/yoyo/Desktop/other/testReport/appiumresult" + timestr + ".html"
    # print(filename)
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #                                    stream=fp,
    #                                    title="testresult",
    #                                    description='testreport'
    #                                    )
    # runner.run(suite)
    # fp.close()
