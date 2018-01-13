# -*- coding: utf-8 -*-

import urllib2
import urllib
import re
import sys
import progressBar,time


def getHTML(url):
    header = {
        # 'Host': 'jandan.net/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Accept-Encoding': 'gzip, deflate',
        # 'Referer': 'http://jandan.net/drawings/page-21',
        # 'Connection': 'keep-alive',
        # 'Cache-Control': 'max-age=0',
    }
    req = urllib2.Request(url,None,header)
    page = urllib2.urlopen(req)
    html = page.read()
    return html

def Schedule(a,b,c):

    '''
     a:已经下载的数据块
     b:数据块的大小
      c:远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100 :
     per = 100
    # print '\r%.2f%%' % per

def getImg(html):
    reg = 'src="(http://.+?\.jpg)"'
    image = re.compile(reg)
    imagelist = re.findall(image,html)
    opener = urllib2.build_opener()
    opener.addheaders = [(
        'User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    )]
    urllib2.install_opener(opener)
    x = 0
    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    for imageUrl in imagelist:
        # urllib.urlopen(imageUrl,"/Users/yoyo/Desktop/other/test/webTest/image/%s.jpg"%x,Schedule)
        req = urllib2.urlopen(imageUrl)
        with open("/Users/yoyo/Desktop/other/test/webTest/image/image-%s.jpg"%x,"wb") as f :
            f.write(req.read())
        x += 1
        # max_steps = 100
        #
        # process_bar = progressBar.ShowProcess(max_steps)
        #
        # for i in range(max_steps + 1):
        #     process_bar.show_process()
        #     time.sleep(0.05)
        # process_bar.close()

    # print imagelist
    return imagelist



if __name__ == '__main__':
    html = getHTML("http://jandan.net/drawings/page-20")
    # html = getHTML("http://www.baidu.com")
    print (html)
    getImg(html)
    print ("-------%s"%getImg(html))