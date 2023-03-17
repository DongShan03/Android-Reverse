import scrapy
from tianya.items import TianyaItem
from redis import Redis 

class GetSpider(scrapy.Spider):
    name = 'get'
    allowed_domains = ['bbs.tianya.cn']
    start_urls = ['http://bbs.tianya.cn/list-666-1.shtml']

    def __init__(self, name=None, **kwargs):
        self.red = Redis(host="localhost", port=6379,
            db=3, decode_responses=True)
        super(GetSpider, self).__init__(name=name, **kwargs)

    def parse(self, response, **kwargs):
        tbodys = response.xpath("//table[@class='tab-bbs-list tab-bbs-list-2']/tbody")[1:]
        for tbody in tbodys:
            hrefs = tbody.xpath("./tr/td[1]/a/@href").extract()
            for href in hrefs:
                detail_url = response.urljoin(href)
                # result = self.red.sadd("天涯:链接", detail_url)
                result = self.red.sismember("天涯:链接", detail_url)  #在集合内则返回1 不在集合内返回0
                if result:
                    print(f"{detail_url}已经抓取过了")
                    continue
                yield scrapy.Request(
                    url=detail_url,
                    callback=self.parse_detail,
                )
        next_page = response.xpath('//div[@class="short-pages-2 clearfix"]/div/a[last()]/@href').extract_first()
        print(next_page)
        yield scrapy.Request(
            url=response.urljoin(next_page),
            callback=self.parse
        )
        
    
    def parse_detail(self, response, **kwargs):
        t = TianyaItem()
        title = response.xpath('//*[@id="post_head"]/h1/span[1]/span/text()').extract_first()
        content = "\n".join(response.xpath('//*[@id="bd"]/div[4]/div[1]/div/div[2]/div[1]/text()').extract())
        t["title"] = title
        t["content"] = content
        self.red.add("天涯:链接", response.url)
        yield t
