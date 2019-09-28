# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/9/20 18:23'
import pandas
import requests,time
import pandas as pd
import numpy as np

r=open(r'od矩阵400.csv','r+',encoding='utf-8')
tmp=pd.read_csv(r)
r.close()

print(tmp.shape)

tmp=tmp.iloc[:,1:]
print(tmp.shape)

sumdd=0

with open(r'test写入OD.csv','w+',encoding='utf-8') as f:
    f.write('o,d,weight,label')
    f.write('\n')
    for row in range(tmp.shape[0]):
        tmp_x=tmp.iloc[row,0]
        tmp_y=tmp.iloc[row,1]
        for col in range(tmp.shape[1]):
            #print(getattr(row, 'c1'), getattr(row, 'c2'))  # 输出每一行
            if tmp.iloc[row,col]!=0:
                f.write(str(row))
                f.write(',')
                f.write(str(col))
                f.write(',')
                sumdd=sumdd+tmp.iloc[row,col]
                f.write(str(tmp.iloc[row,col]))
                #f.write(',')
                #detail, id, name =geocode(str(tmp_x)+','+str(tmp_y))
                #print(detail)
                #f.write(detail)
                f.write('\n')
                #print(getattr(row,col))
print(tmp.iloc[0,0])
print(sumdd)