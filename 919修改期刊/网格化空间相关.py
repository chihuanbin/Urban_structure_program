# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/9/19 19:29'
#也统计前12个空间相关
#牢记这里需要注意的是X,Y关系
# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/9/1 20:38'
import numpy as np
import pandas as pd
from math import radians, sin, cos, asin, sqrt

def haversine(latlon1, latlon2):
    """
    计算两经纬度之间的距离
    """
    #print(type(latlon1))

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

#计算点是否在缓冲区域内,point为np后的
def cal_in_out(point1,area_list,length):
    r_index=-1
    for i in area_list:
        tmp=np.array(i)
        result=haversine(point1,tmp)
        if result<length:
            r_index=area_list.index(i)
            break
    return r_index

Y1=30.529114
Y2=30.809326
X1=103.894287
X2=104.234131
N=20
x_gap=(X2-X1)/N
y_gap=(Y2-Y1)/N

#经度间隔 0.4767285017325457km
#纬度间隔  0.6220706399999973km

index_all=N*N

# def get_mn(X,Y):
#     #利用地板除，刚好返回他们的索引，这样就可以,索引以0开始
#     m=(X-X1)//x_gap
#     n=(Y-Y1)//y_gap
#     #print(m,n)
#     index=(n)*50+m+1
#     return index

def return_cell_grid_id(point):
    #利用地板除，刚好返回他们的索引，这样就可以,索引以0开始
        #print(point[1]) lng
        m=(point[1]-X1)//x_gap
        n=(point[0]-Y1)//y_gap
        #print(m,n)
        index=(n)*20+m+1
        return index

if __name__=='__main__':
    # 初始化读取

    with open('order_20161101.csv', 'r+', encoding='utf-8') as f:
        tmp = f.readlines()

    # with open('800200最终.csv', 'r+', encoding='utf-8') as f:
    #     tmp_point = f.readlines()

    area_list=[]


    ############切记经纬度转换，出现了计算过程就需要30前面120后面
    #30.65964089,104.0743877 #读入聚类点
    # for i in tmp_point:
    #     ttmp=i.split(',')
    #     area_list.append([float(ttmp[0]),float(ttmp[1])])
    # print(area_list)

    # 新建od矩阵，输入点数

    df = pd.DataFrame(np.zeros((index_all, index_all)))
    print(index_all)
    # N = len(area_list)
    # df = pd.DataFrame(np.zeros((N, N)))
    # length = 500
    #
    # print(N)

    for i in tmp:
        #dfjnCh,1478003896,1478005484,104.06576,30.6686,104.062,30.72307
        try:
            tmp_list = i.split(',')
            tmp_oX = float(tmp_list[3])
            tmp_oY = float(tmp_list[4])
            tmp_dX = float(tmp_list[5])
            tmp_dY = float(tmp_list[6])

            ## arr2=np.array([30.58,144.3])
            point_o=np.array([tmp_oY,tmp_oX])
            point_d=np.array([tmp_dY,tmp_dX])

            o_=return_cell_grid_id(point_o)
            d_=return_cell_grid_id(point_d)

            print(o_,d_)

            if o_>0 and o_<=400:
                if d_ > 0 and d_ <= 400:
                    df.iloc[int(o_-1),int(d_-1)] = df.iloc[int(o_-1),int(d_-1)] + 1
        except:
            pass
                #print('处理'+str(o_)+str(d_))

        #cal_in_out(point1,area_list,length):
        # tmp_a=cal_in_out(point_o,area_list,length)
        # tmp_b=cal_in_out(point_d,area_list,length)

        # if tmp_a!=-1 and tmp_b!=-1:
        #     df.iloc[tmp_a,tmp_b]=df.iloc[tmp_a,tmp_b]+1
        #     print(tmp_a,tmp_b,'这里加1')

    df.to_csv('od矩阵400.csv')

    # r2 = open(r'800200最终.csv', 'r+', encoding='utf-8')
    # tmp2 = pd.read_csv(r2, header=None)
