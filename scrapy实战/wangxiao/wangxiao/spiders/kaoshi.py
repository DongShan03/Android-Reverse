import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.cmdline import execute
import json

class KaoshiSpider(scrapy.Spider):
    name = 'kaoshi'
    allowed_domains = ['ks.wangxiao.cn']
    start_urls = ['http://ks.wangxiao.cn/']

    def parse(self, response, **kwargs):
        le = LinkExtractor(restrict_xpaths="//ul[@class='first-title']/li/div/a")
        a_list = le.extract_links(response)[2:]
        for a in a_list:
            first_title = a.text
            url = a.url.replace("TestPaper", "exampoint")
            yield scrapy.Request(
                url = url,
                callback=self.parse_second_level,
                meta={"first_title": first_title},
            )
            break
        
    def parse_second_level(self, response, **kwargs):
        first_title = response.meta["first_title"]
        le = LinkExtractor(restrict_xpaths="//div[@class='filter-item']/a")
        a_list = le.extract_links(response)
        for a in a_list:
            second_title = a.text
            yield scrapy.Request(
                url=a.url,
                callback=self.parse_third_level,
                headers={
                    "Referer": a.url.split("&")[0].replace("exampoint", "TestPaper"),
                },
                meta={"first_title": first_title, "second_title": second_title}
            )
            break
    
    def parse_third_level(self, response, **kwargs):
        first_title = response.meta["first_title"]
        second_title = response.meta["second_title"]
        points = response.xpath("//ul[@class='section-point-item']")
        for point in points:
            p_list = [first_title, second_title]
            parents = point.xpath("./ancestor-or-self::ul[@class='chapter-item' or @class='section-item']")
            for p in parents:
                fu_name = "".join(p.xpath("./li[1]/text()").extract()).strip().replace(" ", "")
                p_list.append(fu_name)
            
            p_name = "".join(point.xpath("./li[1]/text()").extract()).strip().replace(" ", "")

            count = point.xpath("./li[2]/text()").extract_first().split("/")[1]
            sign = point.xpath("./li[3]/span/@data_sign").extract_first()
            subsign = point.xpath("./li[3]/span/@data_subsign").extract_first()

            url = "http://ks.wangxiao.cn/practice/listQuestions" 
            data = {
                "examPointType": "",
                "practiceType": "2",
                "questionType": "",
                "sign": sign, 
                "subsign": subsign,
                "top": count,
            }
            yield scrapy.Request(  # post
                url=url,
                method="POST",
                body=json.dumps(data),  # request payload
                headers={
                    "X-Requested-With": "XMLHttpRequest",
                    "Content-Type": "application/json; charset=UTF-8"
                },
                callback=self.parse_point,
                meta={
                    "p_list": p_list,
                    "p_name": p_name,
                }
            )
            break
        
    def parse_point(self, response, **kwargs):
        p_list = response.meta["p_list"]
        p_name = response.meta["p_name"]
        print(p_list)
        print(response.text)
        # pass


if __name__ == '__main__':
    execute("scrapy crawl kaoshi".split())