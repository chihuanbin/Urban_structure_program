# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/9/5 15:54'
import numpy as np
import pandas as pd
from math import radians, sin, cos, asin, sqrt

def haversine(latlon1, latlon2):
    """
    计算两经纬度之间的距离
    """
    #print(type(latlon1))  numpy.ndarray

    if (latlon1 - latlon2).all():
        lat1, lon1 = latlon1
        lat2, lon2 = latlon2
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6370996.81  # 地球半径
        distance = c * r
    else:
        distance = 0
    return distance

if __name__=='__main__':
    #进行200-500m以内的质心点合并
    with open('800200最终.csv', 'r+', encoding='utf-8') as f:
        #tmp_point = f.readlines()
        df=pd.read_csv(f,header=None)
    #haversine
    print(df)

    N1=df.shape[0]
    print(type(df))
    length=1000


    new_point = []

    import numpy as np
    for i in range(N1):
        julei = []
        julei.append(i)
        for j in range(N1):
            a = np.array([df.iloc[i, 0], df.iloc[i, 1]])
            b = np.array([df.iloc[j, 0,], df.iloc[j, 1]])
            # print(a,b)
            if haversine(a, b) < length:
                julei.append(j)
        sum_x = 0
        sum_y = 0
        print(julei)
        print('###')
        for m in julei:
            sum_x = sum_x + df.iloc[m, 0]
            sum_y = sum_y + df.iloc[m, 1]
        ttmp=[sum_x / len(julei), sum_y / len(julei)]
        new_point.append(ttmp)
        print(ttmp)
        print('$$$')

    print(new_point)
    print(len(new_point))

    formatList = []
    for id in new_point:
        if id not in formatList:
            formatList.append(id)
    print(formatList)
    print(len(formatList))

    # o_=[]
    # n_=[]
    #
    # for i in range(N1):
    #     if i not in result:
    #         new_point.append([df.iloc[i, 0], df.iloc[i, 1]])
    #
    # formatList = []
    # for id in new_point:
    #     if id not in formatList:
    #         formatList.append(id)
    # print(formatList)
    # print(len(formatList))