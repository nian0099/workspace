# -*- coding:UTF-8 -*-
import unittest
import pythontest.Firefox
from selenium import webdriver
import time
import pythontest.kongjian
class tieta(unittest.TestCase):
    def setUp(self):
       self.driver = pythontest.Firefox.starFierFox()
    def tearDown(self):
        pythontest.Firefox.clseFireFox(self.driver)
    def test_t(self):
        pythontest.kongjian.kong(self.driver, self)
        time.sleep(3)
