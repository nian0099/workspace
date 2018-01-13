# -*- coding:UTF-8 -*-
# 解决编码问题
import sys
import unittest

import HTMLTestRunner

from webTest import testunit

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


suit = unittest.TestSuite();
# 将单元测试加入到测试套件里面
suit.addTest(unittest.makeSuite(testunit.tieta));

# 运行单元测试
fileanme = "/Users/yoyo/Desktop/work/report.html";

fw = open(fileanme,"wb");

runner = HTMLTestRunner.HTMLTestRunner(stream = fw ,title=u"统一门户系统",description=u"需求提出");

runner.run(suit);
