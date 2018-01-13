# -*- coding: UTF-8 -*-
import Firefox
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains;
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.command import Command
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

def kong(driver,self):
   driver.find_element_by_xpath(".//*[@id='ul1']/li[6]/form/div/ul/li[6]/a/img").click()
   time.sleep(3)
   msg = driver.find_element_by_id("write_id").text
   ex = u"请输入用户名或密码"
   time.sleep(3)
   self.assertEqual(msg,ex)
   # #账号
   driver.find_element_by_id("j_username").send_keys("lt_zhangjiahong")
   time.sleep(3)
   # #密码
   try:
      WebDriverWait(driver,20).until(lambda x : x.find_element_by_id('j_password'))
   except:
      print u'未找到该元素'
   else:
      print u'找到该元素'
   driver.find_element_by_id("j_password").send_keys("1")
   print u'--->登录'
   time.sleep(3)
   # #登录
   driver.find_element_by_xpath(".//*[@id='ul1']/li[6]/form/div/ul/li[6]/a/img").click()
   time.sleep(3)
   # #需求管理
   driver.find_element_by_xpath(".//*[@id='nav']/dl[4]/dt/a").click()
   time.sleep(3)
   # # 需求提出
   try:
      WebDriverWait(driver,30).until(lambda x : x.find_element_by_xpath(".//*[@id='nav']/dl[4]/dd/ul/li[1]/a"))

   except:
      print u'失败'
   finally:
      print u'成功'
   driver.find_element_by_xpath(".//*[@id='nav']/dl[4]/dd/ul/li[1]/a").click()
   print u'-->点击需求提出'
   time.sleep(3)
   # #定位iframe
   mainframe = driver.find_element_by_id("content_id");
   driver.switch_to_frame(mainframe);
   # #选择数据
   # driver.find_element_by_xpath(".//*[@id='mytable']/tbody/tr/td[1]/div/span").click()
   # time.sleep(3)
   # #删除
   # driver.find_element_by_xpath(".//*[@id='del']").click()
   # time.sleep(3)
   # #点击确认
   # driver.find_element_by_xpath(".//*[@id='confirm']").click()
   # time.sleep(3)
   # #点击确定
   # driver.find_element_by_xpath(".//*[@id='confirm']").click()
   # time.sleep(3)
   # #选择一条数据
   # driver.find_element_by_xpath(".//*[@id='mytable']/tbody/tr/td[1]/div/span").click()
   time.sleep(3)
   # #点击提交
   driver.find_element_by_xpath(".//*[@id='commit']").click()
   print u'-->点击提交'
   # time.sleep(3)
   # #点击确定提交铁塔
   # driver.find_element_by_xpath(".//*[@id='confirm']").click()
   time.sleep(3)
   # #确定退出界面
   driver.find_element_by_xpath(".//*[@id='confirm']").click()
   print u'-->点击确定'
   time.sleep(3)
   # #退出iframe
   driver.switch_to_default_content();
   print u'---over'
   #首页
   driver.find_element_by_xpath(".//*[@id='nav']/dl[1]/dt/a").click()
   time.sleep(3)
   #我的工作台
   driver.find_element_by_xpath(".//*[@id='nav']/dl[2]/dt/a").click()
   time.sleep(3)
   #我的已办
   driver.find_element_by_xpath(".//*[@id='nav']/dl[2]/dd/ul/li[2]/a").click()
   time.sleep(5)
   # #定位iframe
   # driver.switch_to_frame("content_id");
   # driver.switch_to_frame("iframea");
   # #查看
   # driver.find_element_by_xpath(".//*[@id='mytable']/tbody/tr[1]/td[6]/div/a").click()
   # time.sleep(3)
   # driver.switch_to_window(driver.window_handles[1])
   # #driver.find_element_by_xpath(".//*[@id='esc-content']/div/div/div[1]/h2").click()
   # time.sleep(3)
   # driver.close()
   # time.sleep(3)
   # #driver.switch_to_window(driver.window_handles[1])
   # # driver.find_element_by_xpath(".//*[@id='esc-header']/div/div[1]").click()
   # # time.sleep(5)
   #退出
   driver.find_element_by_xpath(".//*[@id='esc-header']/div/div[2]/a[5]").click()
   time.sleep(5)
   
   # #账号宋菁华
   # driver.find_element_by_id("j_username").send_keys("lt_songqinghua")
   # time.sleep(3)
   # # 密码
   # driver.find_element_by_id("j_password").send_keys("1")
   # time.sleep(3)
   # # 登录
   # driver.find_element_by_xpath(".//*[@id='ul1']/li[6]/form/div/ul/li[6]/a/img").click()
   # time.sleep(3)
   # #我的工作台
   # driver.find_element_by_xpath(".//*[@id='nav']/dl[2]/dt/a").click()
   # time.sleep(3)
   # # 我的代办
   # driver.find_element_by_xpath(".//*[@id='nav']/dl[2]/dd/ul/li[1]/a").click()
   # time.sleep(3)
   # driver.switch_to_frame("content_id");
   # driver.switch_to_frame("iframea");
   # driver.find_element_by_xpath(".//*[@id='mytable']/tbody/tr[1]/td[2]/div/span").click()
   # time.sleep(3)
   # driver.find_element_by_xpath(".//*[@id='enter']").click()
   # time.sleep(3)
   # driver.find_element_by_xpath(".//*[@id='dialog-modal']/ul/li[4]/a[1]").click()
   # time.sleep(3)
   # driver.find_element_by_xpath(".//*[@id='confirm']").click()
   # time.sleep(3)
   # driver.find_element_by_xpath(".//*[@id='confirm']").click()
   # time.sleep(3)
   # # 退出iframe
   # driver.switch_to_default_content();
   # # 首页
   # driver.find_element_by_xpath(".//*[@id='nav']/dl[1]/dt/a").click()
   # time.sleep(3)
   # # 退出
   # driver.find_element_by_xpath(".//*[@id='esc-header']/div/div[2]/a[5]").click()
   # time.sleep(5)
   # #账号zhangjiahong
   # driver.find_element_by_id("j_username").send_keys("lt_zhangjiahong")
   # time.sleep(3)
   # # 密码
   # driver.find_element_by_id("j_password").send_keys("1")
   # time.sleep(3)
   # # 登录
   # driver.find_element_by_xpath(".//*[@id='ul1']/li[6]/form/div/ul/li[6]/a/img").click()
   # time.sleep(3)
   # # 我的工作台
   # driver.find_element_by_xpath(".//*[@id='nav']/dl[2]/dt/a").click()
   # time.sleep(3)
   # # 我的代办
   # driver.find_element_by_xpath(".//*[@id='nav']/dl[2]/dd/ul/li[1]/a").click()
   # time.sleep(3)
   # driver.switch_to_frame("content_id");
   # driver.switch_to_frame("iframea");
   # driver.find_element_by_xpath(".//*[@id='mytable']/tbody/tr[1]/td[2]/div/span").click()
   # time.sleep(3)
   # driver.find_element_by_xpath(".//*[@id='enter']").click()
   # time.sleep(3)
   # driver.find_element_by_xpath(".//*[@id='dialog-modal']/ul/li[4]/a[1]").click()
   # time.sleep(3)
   # driver.find_element_by_xpath(".//*[@id='confirm']").click()
   # time.sleep(3)
   # driver.find_element_by_xpath(".//*[@id='confirm']").click()
   # time.sleep(3)
   # ########
   # # # 退出iframe
   # driver.switch_to_default_content();
   # driver.find_element_by_xpath(".//*[@id='nav']/dl[2]/dt/a").click()
   # time.sleep(3)
   # driver.find_element_by_xpath(".//*[@id='nav']/dl[2]/dd/ul/li[2]/a").click()
   # time.sleep(3)
   # #定位iframe
   # driver.switch_to_frame("content_id");
   # driver.switch_to_frame("iframea");
   # #查看
   # driver.find_element_by_xpath(".//*[@id='mytable']/tbody/tr[1]/td[6]/div/a").click()
   # time.sleep(3)
   # driver.switch_to_window(driver.window_handles[1])
   # #driver.find_element_by_xpath(".//*[@id='esc-content']/div/div/div[1]/h2").click()
   # time.sleep(3)
   # driver.close()
   # time.sleep(3)
   #driver.switch_to_window(driver.window_handles[1])
   # driver.find_element_by_xpath(".//*[@id='esc-header']/div/div[1]").click()
   # time.sleep(5)
   ######断言
   #self.assertEqual()




