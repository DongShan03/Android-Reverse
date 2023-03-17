import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ErshouSpider(CrawlSpider):
    name = 'ershou'
    allowed_domains = ['che168.com']
    start_urls = ['http://www.che168.com/beijing/list/#pvareaid=100945']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='viewlist_ul']/li/a", )), callback='parse_item', follow=False),
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='page fn-clear']/a", )), follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath('//div[@class="car-box"]/h3/text()').extract_first()
        item['price'] = response.xpath('//div[@class="left-module block-left"]').extract_first()
        print(item)
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
