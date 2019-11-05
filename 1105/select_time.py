# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 20:24
# @Author  : yemanzhongting
# @Email   : sggzhang@whu.edu.cn
# @File    : select_time.py
# @Software: PyCharm
import configparser
import os, sys
import pandas as pd
class main(object):

    parent_dir = os.path.dirname(os.path.abspath(__file__))

    #  实例化configParser对象
    config = configparser.ConfigParser()
    config.read(parent_dir + "/config.init", encoding='utf-8')  # 读取配置文件采用绝对路径

    # (config.get('environment', 'filename')

    def __init__(self,id):
        self.id=id


if __name__ == '__main__':
    print()
    #利用检索点位，来判断点所在地址
    tmp=pd.read_csv('写入OD.csv',encoding='utf-8')
    df=tmp[tmp.weight>200]
    print(df)
    print(df.shape)
    a={}
    #(lambda x: x * 2 + 10, foo)
    tmp=df['o'].tolist()+df['d'].tolist()
    #function method
    tmp=sorted(list(set(tmp)))
    print(tmp)

    print(type(map(lambda x:{"name":x},tmp)))
    a['nodes']=list(map(lambda x:{"name":str(x)},tmp))
    tmp = df[['o','d','weight']]
    tmp.sort_values(by="o" , ascending=False)
    print((tmp.values.tolist()))#p参数
    result=[]
    for x in tmp.values.tolist():
        if x[0]>x[1]:
            result.append({"source": str(int(x[0])), "target": str(int(x[1])), "value": float(x[2]/10)})
        elif x[0]<x[1]:
            result.append({"source": str(int(x[1])), "target": str(int(x[0])), "value": float(x[2] / 10)})
    a["links"]=result
    # s1 = {"name": ["zhang3", "li4", "wang5"], "age": [16, 20, 18]}
    # temp = []
    # for k in s1:
    #     temp.append([(k, v) for v in s1[k]])
    #
    # print([dict(t) for t in zip(*temp)])

    b={"nodes": [
        {"name": "Agricultural 'waste'"},
        {"name": "Bio-conversion"}],
        "links": [
            {"source": "Agricultural 'waste'", "target": "Bio-conversion", "value": 124.729},
            {"source": "Bio-conversion", "target": "Liquid", "value": 0.597}] }
    #sorted(data, key=lambda d: d['sort_time'], reverse=True)
    print(a)