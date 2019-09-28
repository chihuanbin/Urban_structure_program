# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/9/26 14:48'
import requests,json
url='http://114.116.5.183:12311/roadwatert/getData?stnm=undefined&jswarnlv=undefined&jsz=undefined&jssun=undefined&querytype=zxxx&tmtp=&datatp=all&exportExcel=1'
url2='http://114.116.5.183:12311/roadwatert/getData?stnm=undefined&jswarnlv=undefined&jsz=undefined&jssun=undefined&querytype=zxxx&tmtp=&datatp=all&exportExcel=1'
result=requests.get(url2).text
import jsonpath
data = json.loads(result)
# WORK_LG=jsonpath(data,'$..LGTD')
# WORK_LT=jsonpath(data,'$..lttd')
#
# print(WORK_LG)
# print(WORK_LT)

print(data)
print(type(data))

tmp=data['rows']

n_lgt=[]
n_VENDER=[]
n_ltt=[]
n_time=[]
n_STLC=[]
n_Z=[]
n_text=[]

for i in tmp:
    n_lgt.append(i['LGTD'])
    n_VENDER.append((i['VENDER']))
    n_time.append((i['CREATETIME']))
    n_ltt.append(i['LTTD'])
    n_STLC.append(i['STLC'])
    n_Z.append(i['Z'])
    n_text.append(i['text'])
import pandas as pd

columns = ['LGTD', 'LTTD', 'VENDER','CREATETIME','STLC','Z','text']
tmp_data=[]
for i in range(len(n_lgt)):
    tmp_data.append([n_lgt[i],n_ltt[i],n_VENDER[i],n_time[i],n_STLC[i],n_Z[i],n_text[i]])
save_file = pd.DataFrame(columns=columns, data=tmp_data)

save_file.to_csv('mm2.csv', index=False, encoding="utf-8")