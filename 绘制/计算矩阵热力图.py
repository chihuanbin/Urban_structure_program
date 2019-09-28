# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/8/29 18:02'
import time,datetime

def timeformat_to_timestamp(timeformat=None,format = '%Y-%m-%d %H:%M:%S'):
    # try:
    if timeformat:
        time_tuple = time.strptime(timeformat,format)
        res = time.mktime(time_tuple) #转成时间戳
    else:
        res = time.time()        #获取当前时间戳
    return int(res)

def trans_time(timeStamp):
    dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    return otherStyleTime

# data = {'gridid': [i+1 for i in range(index_all)],
#         'join_count_o':[0 for i in range(index_all)],
#         'join_count_d':[0 for i in range(index_all)],
#         'time_sum':[0 for i in range(index_all)]
#         }

def dec_time(timestamp,start_time,eve_grid):
    n=(timestamp-start_time)/(eve_grid*3600)
    index=int(n)
    return index

start_time='2016-11-07 0:00:00'
markday=1
start_time=timeformat_to_timestamp(start_time)
#1s的3600
#12的3600*2
grid_num=24
eve_grid=24/grid_num

rectangle_table=[0 for i in range(grid_num)]#24格子的
print(rectangle_table)

with open('order_20161107.csv','r+',encoding='utf-8') as f:
    tmp=f.readlines()
for i in range(len(tmp)-1):
    i=i+1
    print(i)
    tmp_list=tmp[i].split(',')

    tmp_time=int(tmp_list[1])#/60#以分钟计时(int(tmp_list[2])-
    print(tmp_time)
    index=dec_time(tmp_time,start_time,eve_grid)
    print(index)
    rectangle_table[index]=rectangle_table[index]+1
    #print(rectangle_table[index])

print(rectangle_table)