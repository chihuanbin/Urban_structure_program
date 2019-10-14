# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/10/8 10:40'
# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/9/29 15:47'
#http://api.map.baidu.com/place/v2/search?query=地铁站&bounds=30.5681733178,103.9560699463,30.7261952729,104.1771697998&page_size=200&page_num=0&output=json&ak=G0m2doGlAZigP3Qsqr8DkVlMGqIRT9dA
#参数1为左下角，参数二为右上角
# 百度地图：http://map.baidu.com/  百度地图poi：http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi
import json
import xlwt
from datetime import datetime
from urllib import request
from urllib.parse import quote
import sys
import time
import base64
from 坐标纠偏 import bd09togcj02,gcj02towgs84

def bdtowgs84(lng,lat):
    tmp=bd09togcj02(lng,lat)
    return gcj02towgs84([tmp[0],tmp[1]])
print(bd09togcj02(128,37))
# 获取当前日期
today = datetime.today()
# 将获取到的datetime对象仅取日期如：2017-4-6
today_date = datetime.date(today)

json_name = 'data_tmap.json'
# 百度地图poi：http://api.map.baidu.com/place/v2/search
# 请替换为自己申请的key值：申请Web服务API类型KEY http://lbsyun.baidu.com/apiconsole/key?application=key
# ak=8VUjfqGwgnHwEZLxwPpnZvO1Sgeq2HFO &tag=医疗
# http://api.map.baidu.com/place/v2/search?query=地铁站&page_size=20&page_num=0&scope=2&region=上海&coord_type=3&output=json&ak=8VUjfqGwgnHwEZLxwPpnZvO1Sgeq2HFO
url_amap = 'http://api.map.baidu.com/place/v2/search?query=地铁站&page_size=20&page_num={page_index}&scope=2&bounds={bounds_area}&coord_type=3&output=json&ak=8VUjfqGwgnHwEZLxwPpnZvO1Sgeq2HFO'
#url_amap = 'http://api.map.baidu.com/place/v2/search?query=卫生服务中心&tag=医疗&page_size=20&page_num=0&scope=2&region=上海市&coord_type=3&output=json&ak=8VUjfqGwgnHwEZLxwPpnZvO1Sgeq2HFO'
#插入检索切片 bounds=23.1121,113.4408,23.212100000000003,113.5408

page_size = 20  # 每页条目数，最大限制为20条
page_index = r'page_num=1'  # 显示页码
total_record = 0  # 定义全局变量，总行数，百度有限制不能超过400条
# Excel表头
hkeys = ['id', '名称', '丛属区划', '从属线路', '北纬', '东经']
# 获取数据列
bkeys = ['uid', 'name', 'area','address',  ['location', 'lat', 'lng']]

u"""
        城市内检索
        百度在没有查找到对应查询请求时, 会返回在其它城市查找到的结果, 返回格式为[{'num': , 'name': ''} ...]这样的数组
        获取一页query相关地理信息
        根据关键词query查找所有地址信息
        *注意* 百度最多返回400条记录
        :param query: 查询关键词
        :param region: 地区
        :param kwargs:
        :return:  if success return
            {
                status: 本次API访问状态, 成功返回0, 其他返回其他数字,
                message: 对本次API访问状态值的英文说明, 如果成功返回'ok', 失败返回错误说明,
                total: 检索总数, 用户请求中设置了page_num字段时才会出现, 当检索总数超过760时, 多次刷新同一请求得到的total值, 可能稍有不同
                results: [
                    {
                        name:  POI名称,
                        location: {
                            lat: 纬度,
                            lng: 经度
                        },
                        address: POI地址信息,
                        telephone: POI电话信息,
                        uid: POI的唯一标识,
                        detail_info: {  # POI扩展信息, 仅当scope=2时, 显示该字段, 不同POI类型, 显示的detail_info字段不同
                            distance: 距离中心点距离,
                            type: POI类型,
                            tag: 标签,
                            detail_url: POI的详情页,
                            price: POI商户的价格,
                            shop_hours: 营业时间,
                            overall_rating: 总体评分,
                            taste_rating: 口味评分,
                            service_rating: 服务评分,
                            environment_rating: 环境评分,
                            facility_rating: 星级评分,
                            hygiene_rating: 卫生评分,
                            technology_rating: 技术评分,
                            image_num: 图片数,
                            groupon_num: 团购数,
                            discount_num: 优惠数,
                            comment_num: 评论数,
                            favorite_num: 收藏数,
                            checkin_num: 签到数
                        }
                    }
                    ...
                ]
            }
            else return None.
        """
# 获取数据
def get_data(pageindex,bounds_area):
    global total_record
    # 暂停500毫秒，防止过快取不到数据
    time.sleep(0.5)
    print('解析页码： ' + str(pageindex) + ' ... ...')
    #url = url_amap.replace('pageindex', str(pageindex))
    url=url_amap.format(page_index=str(pageindex),bounds_area=str(bounds_area))
    # 中文编码
    url = quote(url, safe=',/:?&=')
    html = ""
    print(page_index)
    print(url)
    with request.urlopen(url) as f:
        html = f.read()
    rr = json.loads(html)
    if total_record == 0:
        total_record = int(rr['total'])
    return rr['results']


def getPOIdata(bounds_area):
    global total_record
    print('获取POI数据开始')
    josn_data = get_data(1,bounds_area)
    print(bounds_area)
    if (total_record % page_size) != 0:
        page_number = int(total_record / page_size) + 2
    else:
        page_number = int(total_record / page_size) + 1

    with open(json_name, 'a') as f:
        # 去除最后]
        f.write(json.dumps(josn_data).rstrip(']'))
        print('已保存到json文件：' + json_name)
        for each_page in range(2, page_number):
            print(page_number)
            print(each_page)
            html = json.dumps(get_data(each_page,bounds_area)).lstrip('[').rstrip(']')
            if html:
                html = "," + html
            f.write(html)
            print(html)
            print('已保存到json文件：' + json_name)
        f.write(']')
    print('获取POI数据结束')

def deleteDuplicate(li):
    temp_list=list(set([str(i) for i in li]))
    li=[eval(i) for i in temp_list]
    return li

# 写入数据到excel
def write_data_to_excel(name):
    # 从文件中读取数据
    fp = open(json_name, 'r')
    result = json.loads(fp.read())
    # 实例化一个Workbook()对象(即excel文件)
    #去重

    #result = deleteDuplicate(result)

    wbk = xlwt.Workbook()
    # 新建一个名为Sheet1的excel sheet。此处的cell_overwrite_ok =True是为了能对同一个单元格重复操作。
    sheet = wbk.add_sheet('Sheet1', cell_overwrite_ok=True)

    # 创建表头
    # for循环访问并获取数组下标enumerate函数
    for index, hkey in enumerate(hkeys):
        sheet.write(0, index, hkey)

    # 遍历result中的每个元素。
    print(len(result))
    result = deleteDuplicate(result)
    print(len(result))
    for i in range(len(result)):
        values = result[i]
        n = i + 1
        index = 0
        for key in bkeys:
            val = ""
            islist = type(key) == list#判断列表，就是说是
            import requests
            if islist:
                keyv = key[0]  # 获取属性
                key = key[1:]  # 切片，从第一个开始
                print(keyv)
                print('#')
#c = base64.b64decode(b.encode("utf-8")).decode("utf-8")
                print(key)
                #values[keyv]['lat']  30.6214218784,104.0736421879
                #qgisurl='http://api.gpsspg.com/convert/coord/?oid=23117&key=10509xuv0uw86wx6416x1678w520uv172993y1&from=2&to=0&latlng=22.9621107600,113.9826665700'
                #tmp=requests.get('http://api.map.baidu.com/ag/coord/convert?from=0&to=4&x={}&y={}'.format(values[keyv]['lng'],values[keyv]['lat'])).content
                #tmp=json.loads(tmp)
                tmp=bdtowgs84(values[keyv]['lng'],values[keyv]['lat'])
                for i in (range(2)):
                    val=tmp[i]
                    print(val)
                    # print('1')
                    sheet.write(n, index, val)
                    index = index + 1

                # for ki, kv in enumerate(key):
                #     val = values[keyv][kv]
                #     print(val)
                #     #print('1')
                #     sheet.write(n, index, val)
                #     index = index + 1
            # 判断是否存在属性key
            elif key in values.keys():
                val = values[key]
                sheet.write(n, index, val)
            if not islist:
                index = index + 1
    wbk.save(name + str(today_date) + '.xls')
    print('保存到excel文件： ' + name + str(today_date) + '.xls！')


if __name__ == '__main__':
    # 写入数据到json文件，第二次运行可注释
    #来定义切片操作 3.1121,113.4408,23.212100000000003,113.5408
    ll=(30.5448639409,103.9232768372)
    ph=(30.7672742174,104.1919364418)
    n=3#切成多少等分，n^2
    #bounds=30.5681733178,103.9560699463,30.7261952729,104.1771697998
    x_gap=(ph[0]-ll[0])/n
    y_gap=(ph[1]-ll[1])/n
    for i in range(n):#代表纬度
        for j in range(n):#代表经度
            bounds_area_ll=(ll[0]+(i)*x_gap,ll[1]+(j)*y_gap)
            print(bounds_area_ll)
            bounds_area=str(bounds_area_ll[0])+','+str(bounds_area_ll[1])+','+str(bounds_area_ll[0]+x_gap)+','+str(bounds_area_ll[1]+y_gap)
            getPOIdata(bounds_area)
    # 读取json文件数据写入到excel
    write_data_to_excel("成都地铁站-百度地图纠偏")