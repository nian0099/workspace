# -*- coding: utf-8 -*-

__author__ = 'Mr.汪'

import urllib.parse
import urllib.request
from  html.parser import HTMLParser

class BlogHTMLParser(HTMLParser):
    data = []
    data_key = ""

