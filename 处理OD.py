# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/9/3 16:07'
import pandas
import requests,time
import pandas as pd
import numpy as np

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

r=open(r'od矩阵.csv','r+',encoding='utf-8')
tmp=pd.read_csv(r)
r.close()
r2=open(r'800200最终.csv','r+',encoding='utf-8')
tmp2=pd.read_csv(r2,header=None)
r2.close()
##########这里要删除索引
# tmp=tmp.iloc[1:,:]
# tmp=tmp.iloc[:,1:]

print(type(tmp))
print(tmp.shape)
print(tmp.shape[1])

tmp=tmp.iloc[:,1:]
print(tmp.shape)

print(tmp.shape[0])
print(tmp2.size)

with open(r'写入OD.csv','w+',encoding='utf-8') as f:
    f.write('o,d,weight,label')
    f.write('\n')
    for row in range(tmp.shape[0]):
        tmp_x=tmp2.iloc[row,0]
        tmp_y=tmp2.iloc[row,1]
        for col in range(tmp.shape[1]):
            #print(getattr(row, 'c1'), getattr(row, 'c2'))  # 输出每一行
            if tmp.iloc[row,col]!=0:
                f.write(str(row))
                f.write(',')
                f.write(str(col))
                f.write(',')
                f.write(str(tmp.iloc[row,col]))
                #f.write(',')
                #detail, id, name =geocode(str(tmp_x)+','+str(tmp_y))
                #print(detail)
                #f.write(detail)
                f.write('\n')
                #print(getattr(row,col))
print(tmp.iloc[0,0])

# with open('od矩阵.csv', 'r+', encoding='utf-8') as f:
#     tmp = f.readlines()

# with open('800200最终.csv', 'r+', encoding='utf-8') as f:
#     tmp_point = f.readlines()