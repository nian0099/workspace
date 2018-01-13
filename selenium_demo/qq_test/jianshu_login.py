from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.jianshu.com/sign_in")

# 获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle
#前置当前浏览器窗口
driver.switch_to.window(sreach_windows)

driver.find_element_by_class_name('qq').click()

time.sleep(5)

# 获得当前所有打开的窗口的句柄
all_handles = driver.window_handles

# # 进入注册窗口
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.window(handle)
        print('now register window!')
        # driver.switch_to.frame("login_frame")
        driver.switch_to.frame("ptlogin_iframe")
        driver.find_element_by_id("switcher_plogin").click()
        time.sleep(5)
        # driver.find_element_by_name("account").send_keys('...')
        # driver.find_element_by_name('password').send_keys('...')
        time.sleep(2)
        # ……


driver.quit()

