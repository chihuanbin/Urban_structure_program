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


# if data[i][0] < 30.695 and data[i][0] > 30.660:
#     if data[i][1] < 104.110 and data[i][1] > 104.040:

# Y1=30.660
# Y2=30.695
# X1=104.040
# X2=104.110
# N=20
# x_gap=(X2-X1)/N
# y_gap=(Y2-Y1)/N

Y1=30.529114
Y2=30.809326
X1=103.894287
X2=104.234131
global N
N=100
x_gap=(X2-X1)/N
y_gap=(Y2-Y1)/N

#经度间隔 0.4767285017325457km
#纬度间隔  0.6220706399999973km

index_all=N*N

def get_mn(X,Y):
    #利用地板除，刚好返回他们的索引，这样就可以,索引以0开始
    m=(X-X1)//x_gap
    n=(Y-Y1)//y_gap
    print(m,n)
    index=(n)*N+m+1
    return index

def return_cell_grid_id(point):
    #利用地板除，刚好返回他们的索引，这样就可以,索引以0开始
        #print(point[1]) lng
        m=(point[1]-X1)//x_gap
        n=(point[0]-Y1)//y_gap
        #print(m,n)
        index=(n)*N+m+1
        #print(index)
        index2=[N-n,m]#交换顺序即为
        return index

if __name__=='__main__':
    # 初始化读取
    clus=input('输入聚类个数')
    with open('928800200最终内部小图外侧.csv', 'r+', encoding='utf-8') as f:
        tmp = f.readlines()

    area_list=[]
    # 新建od矩阵，输入点数

    df = pd.DataFrame(np.zeros((int(clus), index_all)))
    print(index_all)

    for i in tmp:
        #dfjnCh,1478003896,1478005484,104.06576,30.6686,104.062,30.72307
        #30.687676,104.108977,0

        tmp_list = i.split(',')
        tmp_oX = float(tmp_list[0])
        tmp_oY = float(tmp_list[1])
        tmp_id = int(tmp_list[2])

        ## arr2=np.array([30.58,144.3])
        point_o=np.array([tmp_oX,tmp_oY])

        o_=int(return_cell_grid_id(point_o))
        print(o_)
        df.iloc[tmp_id,o_]=df.iloc[tmp_id,o_]+1
        #[m,N-n]#m为横轴，n为纵轴
        #df.iloc[int(o_-1),int(d_-1)]
        # if o_>0 and o_<=400:
        #     df.iloc[int(o_-1),int(d_-1)] = df.iloc[int(o_-1),int(d_-1)] + 1

    #df.loc[:, "A"].max()
    new_list=[]
    for indexs in df.columns:#按照列遍历
        #print(df[indexs])
        max=df.loc[:,indexs].max()
        if max!=0:
            #print(type(df.loc[:, indexs]))  <class 'pandas.core.series.Series'>
            max_index=df.loc[:, indexs].tolist().index(max)
            #max_index = np.argmax(df.loc[:,indexs], axis=0)
            new_list.append(max_index)
        else:
            new_list.append(-1)
    df=pd.DataFrame(new_list)
    df.to_csv('od矩阵400.csv')