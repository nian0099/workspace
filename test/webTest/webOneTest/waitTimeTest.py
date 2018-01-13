# coding:utf-8

#导入webdriver模块
from selenium import webdriver
#导入key是为了模拟键盘上的一些操作
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#导入计时器模块
import time
#创建一个浏览器实例，这里用的是mac自带的Safari
browser = webdriver.Chrome()
#这里调用get函数访问"百度"，如果打不开链接，则会一直等待
browser.get('http://www.baidu.com')
#页面加载完成后，判断网页的'title'是否包含"百度"
assert u"百度" in browser.title
try:
    #搜索输入框表格的id为"kw"
    # // *[ @ id = "kw"]
    locator = (By.XPATH,"//*[@id='kw']")
    # locator = (By.ID,"kw")
    elem = WebDriverWait(browser,20).until(EC.presence_of_element_located(locator))
    # elem = WebDriverWait(browser,20).until(lambda x : x.find_element_by_id('kw'))
except:
    print (u'木有找到')
else:
    print (u'找到了')
finally:
    browser.close()
# #在搜索框里输入关键字
# elem.send_keys("今日热点")
# #模拟键盘回车enter提交搜索
# elem.send_keys(Keys.RETURN)
# #等待20s
# time.sleep(5)
# #关闭浏览器
# browser.close()
