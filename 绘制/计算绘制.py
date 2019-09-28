# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/8/30 14:12'
import time,pandas
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
# %config InlineBackend.figure_format = 'svg'
# get_ipython().run_line_magic('matplotlib', 'inline')
# get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'svg'")

time_1101=[4129, 2899, 1843, 1211, 1052, 1093, 2080, 7492, 10450, 13399, 12652, 11885, 11778, 14342, 14703, 13110, 12790, 13280, 12431, 11817, 10808, 10461, 8610, 5108]
time_1102=[3597, 2210, 1392, 887, 894, 843, 1880, 8030, 10774, 13641, 12811, 12703, 12706, 14905, 15140, 13151, 12927, 13868, 13151, 12283, 11837, 10852, 8923, 5244]
time_1103=[3870, 2381, 1539, 996, 964, 923, 1964, 8396, 11456, 13367, 12538, 11856, 12765, 15856, 14852, 13683, 13076, 14159, 13745, 12274, 11626, 11130, 9241, 5649]
time_1104=[3989, 2687, 1699, 1088, 1033, 1018, 2102, 9467, 12216, 14278, 12806, 12513, 13195, 15640, 16269, 15343, 14752, 15513, 14052, 14296, 13201, 12659, 10941, 7001]
time_1105=[5450, 3592, 2357, 1397, 1243, 1333, 2508, 7212, 10984, 12751, 13200, 13963, 13705, 16414, 16321, 14673, 14759, 16710, 15858, 14512, 13681, 12599, 10783, 6806]
time_1106=[5123, 3477, 2268, 1541, 1274, 1046, 1659, 5235, 9198, 11013, 11668, 12674, 13064, 15708, 15594, 14611, 14267, 14901, 14415, 13439, 13111, 11469, 9011, 5264]
time_1107=[3893, 2467, 1584, 980, 984, 1035, 1969, 8267, 10564, 13976, 13377, 12485, 12258, 15785, 15971, 15577, 14783, 14393, 12117, 12192, 11434, 10127, 7937, 4807]

font={
    'weight':'normal',
      'size':12
}

data={
    '1101':time_1101,
    '1102':time_1102,
    '1103':time_1103,
    '1104':time_1104,
    '1105':time_1105,
    '1106':time_1106,
    '1107':time_1107,
}

df = pd.DataFrame(data,index=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])

dft=df.T

print(dft)
print(dft.size)
print(dft.max)


print(dft.stack().idxmax())
print(dft.iloc[5, 17])

#16710

#print(dft.iloc[t])
# pt=df.pivot_table()


plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
import seaborn as sns

f, (ax1) = plt.subplots(figsize = (8,4))#,nrows=2 并列两个

# cmap用cubehelix map颜色
#cmap = sns.cubehelix_palette(start = 1.5, rot = 3, gamma=0.8, as_cmap = True)
#square=True,
sns.heatmap(dft, xticklabels=1,cmap='RdBu_r',linewidths = 0.05, robust=True,ax = ax1, vmin=0,vmax=17000)#RdBu_r sns.cm.rocket_r
ax1.set_title('出行频率热力图',fontdict=font)
ax1.set_xlabel('时间',fontdict=font)

#ax1.set_xticklabels([]) #设置x轴图例为空值

ax1.set_ylabel('日期',fontdict=font)
plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率

plt.show()