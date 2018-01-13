# -*- coding:utf-8 -*-

import urllib.request
import ssl
import json
import cons

ssl._create_default_https_context = ssl._create_unverified_context

station = {}
# 目的是遍历出每个车站的缩写
for i in cons.station_names.split("@"):
    if i:
        tmp = i.split("|")
        station[tmp[1]] = tmp[2]
# print(station["北京"])

# train_date = input("请输入出发时间")
# from_station = station[input("请输入出发城市")]
# to_station = station[input("请输入到达城市")]


train_date = "2017-11-28"
from_station = "DKH"
to_station = "BBH"
# print("station = ",station)

def getList():
    req = urllib.request.Request('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'%(train_date,from_station,to_station))
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
    html = urllib.request.urlopen(req).read()
    dict = json.loads(html)
    result = dict["data"]["result"]
    return result

# c = 0
b = 0
# for i in getList()[b]:
#     for n in i.split("|"):
#         print("[%s],%s"%(c,n))
#         c += 1
#
#     # c = 0
#     print(i)
#
c = 0
bbList = [];
for i in range(0,len(getList())):
    # print("序号：%s   值：%s" % (i + 1, getList()[i]))
    for n in getList()[b].split("|"):
        bbList = n
        # print("[%s],车次：%s"%(c,n))
        c += 1
    b += 1
    c = 0
    break
    #当b = # list数组中数量时调出循环
    # if b >= len(getList()):
    #     break

print("bblist %s"%bbList)

#[3],车次，[8],出发时间，[9],到达时间
# print (getList())

if __name__ == '__main__':
    # train_date = "2017-11-26"
    # from_station = "BJP"
    # to_station = "TJP"
    getList()

