# Urban_structure_program
基于细颗粒度空间网格的城市结构发现研究论文代码托管
论文数据采用滴滴打车某周订单数据，仅研究用！！
数据格式：
订单ID，开始时间戳，结束时间戳，开始经纬度，结束经纬度
omkrLgc56jc5hoAgdjlKqr99764jtwgn,1477964797,1477966507,104.09464,30.703971,104.08927,30.65085

POI是Point of Interest的缩写，中文可以翻译为“兴趣点”。在地理信息系统中，一个POI可以是一栋房子、一个商铺、一个邮筒、一个公交站等。以百度地图为例，将POI分为八类：吃喝、住宿、出行、银行、娱乐、生活、景点、购物，再细一点可以选择大类中的类目。百度地图、高德地图等平台提供了API接口，对接口传入必要的参数，就能返回需要的数据。本节以抓取百度地图广州市医院位置为例进行讲解，主要步骤如下：
（1）	百度地图API Key的获取。API Key是百度地图API必要的请求参数，百度地图开发者平台提供申请入口。
（2）	请求参数。Query参数，即查询的POI种类，本例参数为医院；bounds参数，即检索的区域，格式为lat1，lng1，lat2，lng2；page_size参数，即返回的最大页面数，默认最大为20；page_num参数，即查询第几页的返回数据；region参数，即检索的城市名称；output参数，即查询结果的格式，这里选择json格式；ak参数，即申请的秘钥。详细代码参见github。
（3）	坐标纠偏。由于百度坐标进行了一定加密处理，直接使用坐标会带来很明显的偏差，需要将经纬度从百度坐标系(BD-09)纠偏至CGCS2000或WGS84（两者均为大地坐标系，差异很小），以成都地铁站店为例，给出了纠偏的效果。
