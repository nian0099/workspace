# -*- coding: utf-8 -*-

import unittest

class MyTestCase(unittest.TestCase):


    def test_add_1(self):
        print "123"

    def test_add_2(self):
        print "456"

if __name__ == '__main__':

    unittest.main