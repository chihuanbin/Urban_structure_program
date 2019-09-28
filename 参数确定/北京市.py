# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/8/31 17:14'

import numpy as np, pandas as pd
from sklearn.cluster import DBSCAN
from shapely.geometry import MultiPoint
#import geopandas
import shapefile

from matplotlib import pyplot as plt

plt.title("北京市游客地理标记城区空间聚类结果")


#plt.scatter(latlngs[:, 0], latlngs[:, 1], s=1, c="black", marker='.')
shape_path=r'C:\Users\hp\Desktop\成都\成都论文\成都核心区.shp'

border_shape = shapefile.Reader(shape_path)
border = border_shape.shapes()

plt.show()
# # 聚类中心区域
# def get_centermost_point(cluster):
#     centroid = (MultiPoint(cluster).centroid.x, MultiPoint(cluster).centroid.y)
#     print(centroid)
#     return tuple(centroid)
#
#
# # #渲染聚类结果
# for border_detail in clusters:
#     x, y = [], []
#     for cell in border_detail:
#         x.append(cell[0])
#         y.append(cell[1])
#     plt.scatter(x, y, marker='o')
# plt.show()