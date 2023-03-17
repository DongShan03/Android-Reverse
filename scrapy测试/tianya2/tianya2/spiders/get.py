import scrapy
from scrapy_redis.spiders import RedisSpider, RedisCrawlSpider
from tianya2.items import Tianya2Item

class GetSpider(RedisSpider):
    name = 'get'
    allowed_domains = ['tianya.cn']
    # start_urls = ['http://tianya.cn/']
    redis_key = "ty_start_url"

    def parse(self, response, **kwargs):
        tbodys = response.xpath("//table[@class='tab-bbs-list tab-bbs-list-2']/tbody")[1:]
        for tbody in tbodys:
            hrefs = tbody.xpath("./tr/td[1]/a/@href").extract()
            for href in hrefs:
                detail_url = response.urljoin(href)
                yield scrapy.Request(
                    url=detail_url,
                    callback=self.parse_detail,
                )
        next_page = response.xpath('//div[@class="short-pages-2 clearfix"]/div/a[last()]/@href').extract_first()
        yield scrapy.Request(
            url=response.urljoin(next_page),
            callback=self.parse
        )
        
    
    def parse_detail(self, response, **kwargs):
        t = Tianya2Item()
        title = response.xpath('//*[@id="post_head"]/h1/span[1]/span/text()').extract_first()
        content = "\n".join(response.xpath('//*[@id="bd"]/div[4]/div[1]/div/div[2]/div[1]/text()').extract())
        t["title"] = title
        t["content"] = content
        yield t

