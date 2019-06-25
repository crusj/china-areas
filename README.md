
# china-areas
中国行政区域划分,最新2019-01-31

## 基本信息

* 总45884条记录
* 区域层次

    |省/直辖市|市区|区/县|乡镇/街道办事处|
    |---|---|---|---|
* 字段如下

    |name|code|parent|level|
    |---|---|---|---|
    |名称|统计用区划代码(12位)|父级区划代码|层级|
    

## 用法

* 安装python,以及爬虫框架scrapy(`pip3 install scrapy`)
* 生成**csv**文件:进入项目根目录 `scrapy crawl area -o area.json`
* 生成**json**文件:进入项目根目录 `scrapy crawl area -o area.csv`
* 项目根目录下已经包含最新拉取的json以及csv文件

## 导入mysql

### 表结构

```sql
CREATE TABLE `area` (
  `name` varchar(20) NOT NULL COMMENT '名称',
  `code` varchar(15) NOT NULL COMMENT '区划代码',
  `parent` varchar(15) NOT NULL COMMENT '父级',
  `level` tinyint(3) unsigned NOT NULL COMMENT '层级',
  UNIQUE KEY `areas_UN` (`code`),
  KEY `areas_parent_IDX` (`parent`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='中国区域划分表'


可能出现错误`mysqlimport: Error: 1148, The used command is not allowed with this MySQL version`
需要在mysql客户端执行`set global local_infile = 'ON';`
```

### 导入命令

```shell
mysqlimport --ignore-lines=1 \
    --fields-terminated-by=, \
   --host=host \
   --local -u root \
   -p database \
   area.csv
```

其中host为主机名,database为数据库名,area.csv为文件名，area为表名
