import scrapy


class TupianSpider(scrapy.Spider):
    name = 'tupian'
    allowed_domains = ['tupianzj.com']
    start_urls = ['https://www.tupianzj.com/sheying/spc/caobenzhiwu/']

    def parse(self, response, **kwargs):
        print(response.text)
        li_list = response.xpath("//ul[@class='d1 ico3']/li")
        print(li_list)
        for li in li_list:
            href = li.xpath("./div/a/@href")#.extract_first()
            print(href)
            yield scrapy.Request(
                url=response.urljoin(href),
                method='GET',
                callback=self.parse_detail
            )
    
    def parse_detail(self, response, **kwargs):
        pass
            
