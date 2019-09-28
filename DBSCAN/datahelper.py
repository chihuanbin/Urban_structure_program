# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/8/29 21:38'
import matplotlib.pyplot as plt
import numpy as np
import random

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']


# 随机生成大致是K个类别的点，用均匀分布生成中心点的位置，用高斯分布生成中心点周围的点
def generatorN(K):
    # np.random.seed()
    center = [[np.random.rand(1) * 20, np.random.rand(1) * 20] for _ in range(K)]
    _data = []
    for _x, _y in center:
        _data.append([np.random.randn(100) + _x, np.random.randn(100) + _y])

    _data = np.transpose(_data, (0, 2, 1)).reshape((-1, 2))

    np.random.shuffle(_data)
    return _data


# 画图
def draw_data(_groups):
    # fig=plt.figure(dpi=180)
    plt.title("画图")
    for xys in _groups.values():
        xs = [xy[0] for xy in xys]
        ys = [xy[1] for xy in xys]
        plt.scatter(xs, ys)
    plt.show()