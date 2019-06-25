
# china-areas
中国行政区域划分,最新2019-01-31

## 基本信息
* 总45884条记录
* 区域层次,省/直辖市 =>市 区/县=>乡镇/街道办事处
* 字段,name=>名称,code=>统计用区划代码,parent=>父级统计用区划代码,level=>层级

## 用法

* 安装python,以及爬虫框架scrapy
* 生成**csv**文件:进入项目根目录 `scrapy crawl area -o area.json`
* 生成**json**文件:进入项目根目录 `scrapy crawl area -o area.csv`
* 项目根目录下已经包含最新拉去的json以及csv文件

