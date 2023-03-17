import scrapy
from caipiao.items import CaipiaoItem

class ShuangseqiuSpider(scrapy.Spider):
    name = 'shuangseqiu'
    allowed_domains = ['500.com']
    start_urls = ['https://datachart.500.com/ssq/']

    def parse(self, response, **kwargs):
        trs = response.xpath("//tbody[@id='tdata']/tr")
        for tr in trs:
            if tr.xpath("./@class").extract_first() == "tdbck":
                continue
            # red_ball = tr.xpath("./td[@class='chartBall01']/text()").extract()
            red_ball = " ".join(tr.css(".chartBall01::text").extract())
            blue_ball = tr.css(".chartBall02::text").extract()[0]
            qihao = tr.xpath("./td[@align='center']/text()").extract()[0].strip()

            item = CaipiaoItem()
            item['qihao'] = qihao
            item['blue_ball'] = blue_ball
            item["red_ball"] = red_ball

            yield item

