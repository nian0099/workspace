#coding:utf-8

import screenshotTest
from appium import webdriver
import time


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = 'oneplus-a0001-ae45407'
desired_caps['appPackage'] = 'philm.vilo.im'
desired_caps['appActivity'] = 'philm.vilo.im.android.MainActivity'


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# elem = driver.find_element_by_xpath(".//*[@resource-id='philm.vilo.im:id/top_image']").click()
# loc_id = 'resourceId("philm.vilo.im:id/top_image").index(2)'
# elem = driver.find_elements_by_android_uiautomator(loc_id).click()
# elem.click()

# el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.ImageView")
# el1.click()

# driver.wait_activity("philm.vilo.im.android.MainActivity",30)

# driver.find_element_by_class_name("android.view.View").click()

# try:
#     elem = driver.find_element_by_class_name('android.widget.ImageView')
#     elem.click()
#
# except:
#     print u'error'
# finally:
#     print u'完事了'
#在一加手机上可以使用，不同系统可能会有兼容性问题by___resourceId,顺序是从0开始
# driver.find_elements_by_id("philm.vilo.im:id/top_image")[1].click()
#在一加手机上可以使用，不同系统可能会有兼容性问题by___resourceId,顺序是从1开始
driver.find_elements_by_class_name("android.widget.ImageView")[1].click()

# driver.find_element_by_android_uiautomator(loc_id).click()
screenshotTest.screenshot()

time.sleep(3)
# driver.find_element_by_link_text("1").click()
#
# driver.find_element_by_link_text("5").click()
#
# driver.find_element_by_link_text("9").click()
#
# driver.find_element_by_link_text("delete").click()
#
# driver.find_element_by_link_text("9").click()
#
# driver.find_element_by_link_text("5").click()
#
# driver.find_element_by_link_text("+").click()
#
# driver.find_element_by_link_text("6").click()
#
# driver.find_element_by_link_text("=").click()

driver.quit()
