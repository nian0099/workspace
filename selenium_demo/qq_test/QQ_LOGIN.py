# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

# 进入浏览器设置
# options = webdriver.ChromeOptions()
# 设置中文
# options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
# options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')

# browser = webdriver.Chrome(chrome_options=options)

browser = webdriver.Chrome()

browser.get("http://id.qq.com")

# browser.maximize_window()

browser.switch_to.frame("login_frame")

elem = browser.find_element_by_id("switcher_plogin").click()

time.sleep(3)

elem2 = browser.find_element_by_id("switcher_qlogin").click()

time.sleep(3)

browser.close()

