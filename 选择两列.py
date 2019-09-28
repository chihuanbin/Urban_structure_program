# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/8/31 15:57'
import pandas as pd
with open('order_20161101.csv','r+',encoding='utf-8') as f:
    tmp=f.readlines()
data = {'x': [i+1 for i in range(len(tmp)-1)],
        'y':[0 for i in range(len(tmp)-1)],
        }
df = pd.DataFrame(data)

print(df)
print(df.size)

# with open('order_20161101_w.csv','w+',encoding='utf-8') as f:
for i in range(len(tmp)-1):
    i=i+1
    #print(i)
    tmp_list=tmp[i].split(',')

    df.iloc[i,0]=tmp_list[3]
    df.iloc[i, 1] = tmp_list[4]

df.to_csv(r'tmp_2.csv', sep=',',header=True, index=False)