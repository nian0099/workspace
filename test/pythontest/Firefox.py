# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
def starFierFox():
    # driver = webdriver.Firefox()
    driver = webdriver.Firefox(executable_path = '/Users/yoyo/Desktop/test/geckodriver')
    driver.implicitly_wait(30)
    url = "http://123.126.34.27:18180/portal/login/getLoginPage"
    driver.get(url)

    driver.maximize_window()
    time.sleep(3)

    return driver
def closeFireFox(driver):
    driver.quit()