# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/9/4 17:37'
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


if __name__=='__main__':
    #进行200-500m以内的质心点合并
    with open('800200最终.csv', 'r+', encoding='utf-8') as f:
        #tmp_point = f.readlines()
        df=pd.read_csv(f)
    #haversine
    print(df)

    N1=df.shape[0]
    print(type(df))
    print('开始有 %d 个聚类点'%N1)
    length = 10000

    t_df = np.array(df)
    tmp = t_df.tolist()  #
    print(tmp)

    area_list=tmp

    new_tmp=[]
    for i in tmp:
        new_tmp.append([(i[0],i[1])])
    print(new_tmp)

    df2 = pd.DataFrame(np.zeros((N1, N1)))


    for i in tmp:
        point_o = np.array(i)
        #     point_d = np.array([tmp_dY, tmp_dX])
        for j in tmp:
            point_d = np.array(j)
            tmp_dis=haversine(point_o,point_d)
            if tmp_dis<length:
                a=tmp.index(i)
                b=tmp.index(j)
                print(a,b)
                df2.iloc[a,b]=df2.iloc[a,b]+1

    #print(df)
    od_list=[]
    for i in range(N1):
        # dict_ = dict(df.loc[i].value_counts())
        # print(dict_)
        # print(dict_[1])
        for j in range(N1):
            if df2.iloc[i,j]!=0:
                if i!=j:
                    if i>j:
                        od_list.append([j,i])
                    else:
                        od_list.append([i, j])
    print(od_list)
    print(len(od_list))

    formatList = []
    for id in od_list:
        if id not in formatList:
            formatList.append(id)
    print(formatList)
    print(len(formatList))
    #刚好是矩阵的1/2

    i_point=[]
    #主要点
    o_point=[]
    #边点
    i_point_list=[]
    #主要点集合

    # for i in range(len(formatList)):
    #     for j in formatList:
    #         if i in j:

    i_point_list=[[] for i in range(len(formatList))]
    print(i_point_list)

    for i in formatList:
        #i_point_list[formatList.index(i)] = []
        for j in i:
            for k in formatList:
                if j in k:
                    i_point_list[formatList.index(i)].append(k)

    print(i_point_list)#[[[0, 23], [0, 23]], [[3, 18], [3, 18]], [[4, 19], [4, 21], [4, 19], [6, 19], [12, 19]],

    print(len(i_point_list))

    new_list=[]
    for i in i_point_list:#[[0, 23], [0, 23]]
        a= set()
        for j in i:#[0, 23]
            for k in j:#[0
                a.add(k)
        print(a)
        #print(type(a))#set
        new_list.append(list(a))

    result=[]#list(c)


    for i in new_list:#[42, 38, 39]
        for j in i:#数字42,
            if j not in result:
                result.append(j)
    print(result)

    tmp=result
    julei = []
    new_point=[]
    for i in result:
        julei.append(i)
        for j in tmp:
            a=np.array([df.iloc[i,0],df.iloc[i,1]])
            b=np.array([df.iloc[j,0,],df.iloc[j,1]])
            #print(a,b)
            if haversine(a,b)<length:
                julei.append(j)
        sum_x=0
        sum_y=0
        for m in julei:
            sum_x=sum_x+df.iloc[m,0]
            sum_y=sum_y+df.iloc[m,1]
        new_point.append([sum_x/len(julei),sum_y/len(julei)])


    print((new_point))
    for i in range(N1):
        if i not in result:
            new_point.append([df.iloc[i,0],df.iloc[i,1]])
    #haversine()

    #for i in
    formatList=[]
    for id in new_point:
        if id not in formatList:
            formatList.append(id)
    print(formatList)
    print(len(formatList))

    # i_point.append(i[0])
    # o_point.append(i[1])
    #
    # for j in range(len(formatList)):
    #     if :
    #     else:
    #         o_point.append()
    # i_point.append(i[0])

    #print((df == 0).astype(int).sum(axis=1))

    N2=0
    #划分为N2个新聚类，聚类有节点
    #for i in range(N1):


    #df.to_csv('测试之心点合并.csv')
    # for i in range(N1):
    #     tmp[i]#其中一个XY数据
    #     for j in new_tmp:
    #         for k in j:
    #             # k为tuple)
    #            if k!=tmp[i]:
    #                if dist[k, tmp[i]] < length:
    #                    new_tmp=
    # for i in

    # for i in range(N1):
    #
    #     # dfjnCh,1478003896,1478005484,104.06576,30.6686,104.062,30.72307
    #     tmp_list = i.split(',')
    #     tmp_oX = float(tmp_list[3])
    #     tmp_oY = float(tmp_list[4])
    #     tmp_dX = float(tmp_list[5])
    #     tmp_dY = float(tmp_list[6])
    #
    #     ## arr2=np.array([30.58,144.3])
    #     point_o = np.array([tmp_oY, tmp_oX])
    #     point_d = np.array([tmp_dY, tmp_dX])
    #
    #     # cal_in_out(point1,area_list,length):
    #     tmp_a = cal_in_out(point_o, area_list, length)
    #     tmp_b = cal_in_out(point_d, area_list, length)
    #     if tmp_a != -1 and tmp_b != -1:
    #         df.iloc[tmp_a, tmp_b] = df.iloc[tmp_a, tmp_b] + 1
    #         print(tmp_a, tmp_b, '这里加1')
    #
    # df.to_csv('od矩阵.csv')

    # import numpy as np
    #
    # a = np.array([(tag, 23.00, 5), (tag2, 25.00, 10)])
    # unique_tags = np.unique(a[0, :])  # note the slicing of the array
    # 现在计算每个标签的平均值
    # meandic = {}
    # for element in unique_tags:
    #     tags = np.nonzero(a[0, :] == element)  # identify which lines are tagged with element
    #     meandic[element] = np.mean([t(1) * t(2) for t in a[tags]])
