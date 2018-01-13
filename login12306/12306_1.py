# -*- coding:utf-8 -*-

import urllib.request
import ssl
import json
import cons
import time

City = {}


def setCity(city):
    for i in cons.station_names.split("@"):
        if i:
            tmp = i.split("|")
            City[tmp[1]] = tmp[2]


def getStation(Station):
    try:
        Station = City[Station]
    except Exception as e:
        print ('City Error')
        return None
    return Station


def setStation(from_station, to_station, queryDate, purpose_codes):
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=%s' % (
    queryDate, from_station, to_station, purpose_codes)
    return url


def getList(url):
    html = urllib.request.urlopen(url)
    text = json.loads(html.read())  # 这样处理起来比较简单 将 str 变换为Json 类型
    return text


def sendToPhone(text):
    pass


if __name__ == '__main__':
    from_station = '西安'
    to_station = '临河'
    queryDate = '2017-11-26'
    purpose_codes = 'ADULT'
    yw_Count = 0
    yz_Count = 0

    # 获得城市字典
    setCity(City)
    # 查询城市代码
    from_station = getStation(from_station)
    to_station = getStation(to_station)

    # 设置查询Url
    url = setStation(from_station, to_station, queryDate, purpose_codes)

    # 进行get请求 获取数据
    text = ''

    # 当 车票信息不存在 datas 下的数据为空
    try:
        Data = getList(url)['data']
        bHaveTicket = True
    except Exception as e:
        print
        '没有查询到车辆信息'
        bHaveTicket = False

    # 解析车辆信息
    if bHaveTicket:
        for index in range(0, len(Data)):
            try:
                yw_Count = Data[index]['queryLeftNewDTO']['yw_num']
                yz_Count = Data[index]['queryLeftNewDTO']['yz_num']
            except Exception as e:
                yw_Count = 0
                yz_Count = 0

            textmp = u'''
        车次: %s %s - %s
        出发时间:%s %s
        历时:%s
        卧铺信息: 硬卧: %s, 软卧: %s, 硬座: %s ,无座: %s \n
        ''' % (
            Data[index]['queryLeftNewDTO']['station_train_code'], Data[index]['queryLeftNewDTO']['from_station_name'],
            Data[index]['queryLeftNewDTO']['to_station_name'], Data[index]['queryLeftNewDTO']['start_train_date'],
            Data[index]['queryLeftNewDTO']['start_time'], Data[index]['queryLeftNewDTO']['lishi'],
            Data[index]['queryLeftNewDTO']['yw_num'],
            Data[index]['queryLeftNewDTO']['rw_num'], Data[index]['queryLeftNewDTO']['yz_num'],
            Data[index]['queryLeftNewDTO']['wz_num'])
            if yw_Count != 0 or yz_Count != 0:
                text += textmp
            else:
                print
                textmp
                # print u'\t\t %s 卖完了！！ 让你不早买。。。'%Data['station_train_code']
                pass
        print
        text
        print
        '检测时间： %s' % time.strftime('%Y-%m-%d %H:%S:%M')
        print
        '|----------23:00-06:00系统维护时间-------------|'