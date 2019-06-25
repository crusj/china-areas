import scrapy


class AreaSpider(scrapy.Spider):
    name = "area"
    base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/'
    start_urls = [
        'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/index.html',
    ]

    def parse(self, response):
        for province in response.css('table.provincetable tr.provincetr a'):
            href = province.attrib['href']
            name = province.xpath("text()").get()
            code = href.split('.')[0].ljust(12, '0')
            yield {
                "name": name,
                "code": code,
                "parent": "0",
                "level": 1
            }
            if href is not None:
                yield response.follow(href, callback=lambda response, pcode=code: self.parse_city(response, pcode))

    def parse_city(self, response, pcode):
        for city in response.css('table.citytable tr.citytr'):
            href = city.xpath('.//td[1]/a/@href').get()
            code = city.xpath('.//td[1]/a/text()').get()
            name = city.xpath('.//td[2]/a/text()').get()
            yield {
                "name": name,
                "code": code,
                "parent": pcode,
                "level": 2
            }
            if href is not None:
                yield response.follow(href, callback=lambda response, pcode=code: self.parse_county(response, pcode))

    def parse_county(self, response, pcode):
        for county in response.css('table.countytable').xpath('.//tr[2]/following-sibling::*'):
            href = county.xpath('.//td[1]/a/@href').get()
            code = county.xpath('.//td[1]/a/text()').get()
            name = county.xpath('.//td[2]/a/text()').get()
            yield {
                "name": name,
                "code": code,
                "parent": pcode,
                "level": 3
            }
            if href is not None:
                yield response.follow(href, callback=lambda response, pcode=code: self.parse_town(response, pcode))

    def parse_town(self, response, pcode):
        for town in response.css('table.towntable tr.towntr'):
            href = town.xpath('.//td[1]/a/@href').get()
            code = town.xpath('.//td[1]/a/text()').get()
            name = town.xpath('.//td[2]/a/text()').get()
            yield {
                "name": name,
                "code": code,
                "parent": pcode,
                "level": 4
            }
