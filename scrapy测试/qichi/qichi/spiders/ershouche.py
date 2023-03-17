import scrapy
from scrapy.linkextractors import LinkExtractor

class ErshoucheSpider(scrapy.Spider):
    name = 'ershouche'
    allowed_domains = ['che168.com']
    start_urls = ['http://www.che168.com/beijing/list/#pvareaid=100945']

    def parse(self, response, **kwargs):
        # hrefs = response.xpath("//ul[@class='viewlist_ul']/li/a/@href").extract()
        # for href in hrefs:
        #     yield scrapy.Request(
        #         url=response.urljoin(href),
        #         callback=self.parse_details,
        #     )
        le = LinkExtractor(restrict_xpaths=("//ul[@class='viewlist_ul']/li/a", ))
        links = le.extract_links(response)
        for link in links:
            yield scrapy.Request(
                url=link.url,
                callback=self.parse_details
            )
        page_le = LinkExtractor(restrict_xpaths=("//div[@class='page fn-clear']/a", ))
        page_links = page_le.extract_links(response)
        # print(page_link.url)
        for link in page_links:
            yield scrapy.Request(
                url=link.url,  #自动去重
                callback=self.parse
            )
    def parse_details(self, response, **kwargs):
        print(response.url)