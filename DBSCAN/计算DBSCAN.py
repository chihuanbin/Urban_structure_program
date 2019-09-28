# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/8/29 21:39'
# DBSCAN

import datahelper

# 判断是不是已经分好簇了
def in_groups(_x, _y):
    for xys in groups.values():
        for p_x, p_y in xys:

            if p_x == _x and p_y == _y:
                return True
    return False


# 获取一个点所有的邻居
def get_neighbors(_x, _y):
    _neighbors = []
    for p_x, p_y in data:
        if p_x == _x and p_y == _y:  # 自己不是自己的邻居
            continue
        if (p_x - _x) ** 2 + (p_y - _y) ** 2 <= distance_thresh:
            _neighbors.append([p_x, p_y])

    return _neighbors


def get_grouped_pts():
    _count = 0
    for xys in groups.values():
        _count += len(xys)
    return _count


def get_ungrouped_p():
    for p_x, p_y in data:
        if not in_groups(p_x, p_y):
            return p_x, p_y
    return None


# groups
min_pts = 13
distance_thresh = 2.35
groups = {}
# 存放聚类信息，格式（x,y）:[[x1,y1],[x2,y2]...],xy是这个簇中最先被选中的点

with open('order_20161101_w.csv','r+',encoding='utf-8') as f:
    tmp=f.readlines()

all_rows=len(tmp)-1
print(all_rows)

datax=[]
datay=[]
for i in range(all_rows):
    i=i+1
    tmp_list = tmp[i].split(',')
    # tmp_time = (int(tmp_list[2]) - int(tmp_list[1])) / 60  # 以分钟计时
    tmp_oX = float(tmp_list[3])
    tmp_oY = float(tmp_list[4])
    datax.append(tmp_oX)
    datay.append(tmp_oY)

data = {
        'x':datax,
        'y':datay
        }

import pandas as pd

df = pd.DataFrame(data)
data=df.as_matrix()

#data = datahelper.generatorN(5)  # 生成原始数据

print(len(data))
print(type(data))
print(data.size)

judged = []  # 判断某个点有没有被判断过
count = 0
while len(data) != get_grouped_pts():
    x, y = get_ungrouped_p()
    stack = [[x, y]]
    groups[(x, y)] = [[x, y]]
    # 把这个点可以连接到的点加入整个簇
    while len(stack) != 0:
        x_, y_ = stack.pop()
        neighbors = get_neighbors(x_, y_)
        if len(neighbors) >= min_pts:
            for neighbor in neighbors:
                if neighbor not in judged:
                    stack.append(neighbor)
                    judged.append(neighbor)
            for neighbor in neighbors:
                if not in_groups(*neighbor):
                    groups[(x, y)].append(neighbor)
datahelper.draw_data(groups)