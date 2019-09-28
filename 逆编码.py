# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/9/3 16:58'

import requests


# 我这里是将经纬度转换为地址，所以选用的是逆地理编码的接口。
# https://restapi.amap.com/v3/geocode/regeo?
# output=xml&location=116.310003,39.991957&key=<用户的key>&radius=1000&extensions=all

# 高德地图
def geocode1(location):
    parameters = {'output': 'json', 'location': location, 'key': 'fd8ac4def17b154976d096a2b784da80',
                  'extensions': 'all'}
    base = 'https://restapi.amap.com/v3/geocode/regeo'
    response = requests.get(base, parameters)
    answer = response.json()
    print('url:' + response.url)
    print(answer)
    return answer['regeocode']['formatted_address'], answer['regeocode']['roads'][0]['id'], \
           answer['regeocode']['roads'][0]['name']


# 百度地图
def geocode(location):
    parameters = {'location': location, 'output': 'json', 'coordtype': 'gcj02ll',
                  'pois': '0', 'latest_admin': '1', 'ak': 'FUu6OTikvprEEwd1qL9X23a9PGq05efW', 'extensions_road': 'true'}
    base = 'http://api.map.baidu.com/geocoder/v2/'
    response = requests.get(base, parameters)
    # response=requests.get('http://api.map.baidu.com/geocoder/v2/?location=30.48686,104.07649&output=json&pois=1&latest_admin=1&ak=U1ck8zXZpoWGYqv2ozr8Xa3IraDfy4Vw')
    print('url:' + response.url)
    answer = response.json()
    print(answer)
    return answer['result']['formatted_address'], answer['result']['addressComponent']['adcode'], \
           answer['result']['addressComponent']['street']


xtmp = 104.0869634
ytmp = 30.63872544
#30.63872544,104.0869634
locations = str(ytmp) + ',' + str(xtmp)
detail, id, name = geocode(locations)
print(detail)
print(id)
print('@@@@@@')
locations = str(xtmp) + ',' + str(ytmp)
print(geocode1(locations))
