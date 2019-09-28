# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/8/30 16:32'
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from math import radians, sin, cos, asin, sqrt

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

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

tmp_list_xy=[]

if __name__ == "__main__":
    data = []
    with open('order_20161101_w.csv', 'r+', encoding='utf-8') as f:
        tmp = f.readlines()
    for i in tmp:
        tmp_list = i.split(',')
        tmp_oX = float(tmp_list[3])
        tmp_oY = float(tmp_list[4])
        data.append([ tmp_oY,tmp_oX])
    data = np.array(data)

    print(data.size)

    ################这里
    MinPts = int(data.shape[0] / 100)
    eps = 500

    db = DBSCAN(eps=eps, min_samples=MinPts, metric=haversine).fit(data)#metric计算特征向量之间的距离

    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    #print(labels)  [-1 -1  0  0  0  0 -1 -1]
    print('看上面')
    print(len(labels))

    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

    unique_labels = set(labels)

    means_num=(len(unique_labels)-1)

    from numpy import linspace
    from matplotlib import cm

    start = 0.0
    stop = 1.0
    number_of_lines = means_num
    cm_subsection = linspace(start, stop, number_of_lines)
    colors = [cm.jet(x) for x in cm_subsection]
    #colors = ['r', 'b', 'g', 'y', 'c', 'm', (0.0, 0.0, 0.5, 1.0),'orange']

    print(unique_labels )

    # >> > a = [1, 2, 3]
    # >> > b = [4, 5, 6]
    # >> > c = [4, 5, 6, 7, 8]
    # >> > zipped = zip(a, b)  # 打包为元组的列表
    # [(1, 4), (2, 5), (3, 6)]

    for k, col in zip(unique_labels, colors):
        if k == -1:
            col = 'k'
        class_member_mask = (labels == k)

        # print(class_member_mask)
        # print('###')
        # print(core_samples_mask)
        # print('---------------')
        # print(class_member_mask & core_samples_mask)

        xy = data[class_member_mask & core_samples_mask]
        #此时求均值
        print(type(xy))
        print(np.mean(xy[:,0]))
        print(len(xy))

        tmp_list_xy.append([np.mean(xy[:,0]),np.mean(xy[:,1])])
        #for i_tmp in xy:


        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='w', markersize=10)
        print('----分割线----')
        xy = data[class_member_mask & ~core_samples_mask]
        #print(xy)
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='w', markersize=3)

    print(tmp_list_xy)

    with open('point.csv','w+',encoding='utf-8') as f:
        for i in tmp_list_xy:
            f.write(str(i[0])+','+str(i[1]))
            f.write('\n')

    plt.title('估计聚类数: %d' % n_clusters_)
    plt.show()
