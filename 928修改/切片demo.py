# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/10/8 13:20'
# -*- coding: utf-8 -*-
# Python 2.7
# 提取城市的POI点信息并将其保存至MongoDB数据库
import requests,requests
import json
import pymongo
from pymongo import MongoClient
left_bottom = [103.9232768372,30.5448639409] # 设置区域左下角坐标（百度坐标系）
right_top = [104.1919364418,30.7672742174] # 设置区域右上角坐标（百度坐标系）
part_n = 2 # 设置区域网格（2*2）

client = pymongo.MongoClient('127.0.0.1', 27017)  # 缺少一步骤进行属性的清洗操作，确定是否有这个值
db = client.test
dbname = 'subway'

url0 = 'http://api.map.baidu.com/place/v2/search?'
x_item = (right_top[0]-left_bottom[0])/part_n
y_item = (right_top[1]-left_bottom[1])/part_n
query = '地铁站' #搜索关键词设置
ak = '8VUjfqGwgnHwEZLxwPpnZvO1Sgeq2HFO' #百度地图api信令
n = 0 # 切片计数器
for i in range(part_n):
    for j in range(part_n):
        left_bottom_part = [left_bottom[0]+i*x_item,left_bottom[1]+j*y_item] # 切片的左下角坐标
        right_top_part = [right_top[0]+i*x_item,right_top[1]+j*y_item] # 切片的右上角坐标
        for k in range(20):
            url = url0 + 'query=' + query + '&page_size=20&page_num=' + str(k) + '&scope=1&bounds=' + str(left_bottom_part[1]) + ',' + str(left_bottom_part[0]) + ','+str(right_top_part[1]) + ',' + str(right_top_part[0]) + '&output=json&ak=' + ak
            data2 = requests.get(url)
            a=data2.text
            print(a)
            hjson = json.loads((data2.text))
            if hjson['message'] == 'ok':
                results = hjson['results']
                for m in range(len(results)) :# 提取返回的结果
                    db[dbname].insert_one(results[m])
        n=n+1
print('第'+str(n)+'个切片入库成功')