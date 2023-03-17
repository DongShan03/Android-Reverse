import scrapy
from scrapy_splash import SplashRequest
from scrapy_redis.spiders import RedisSpider
from splash_test.items import SplashTestItem

lua_source = """
function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  
  get_btn_display = splash:jsfunc([[
    function(){
      return document.getElementsByClassName("load_more_btn")[0].style.display
    }
    ]])
  while(true)
  do
    splash:runjs("document.getElementsByClassName('load_more_btn')[0].scrollIntoView[true]")
    splash:select(".load_more_btn").click()
    splash:wait(1)
    display = get_btn_display()
    if (display == "none")
      then
      	break
      end
  end
  return splash:html()
end
"""


class TestSpider(RedisSpider):
    name = 'test'
    allowed_domains = ['news.163.com']
    start_urls = ['http://news.163.com/']
    # redis_key = "wangyi:news:start_urls"

    def start_requests(self):
        yield SplashRequest(
            url=self.start_urls[0],
            callback=self.parse,
            endpoint="execute",
            args={
                "lua_source": lua_source,
            },
            dont_filter=True
        )

    def parse(self, response):
        divs = response.xpath("//div[@class='ndi_main']/div")
        for div in divs:
            a = div.xpath("./div/div/h3/a")
            if not a:
                continue
            a = a[0]
            splash_item = SplashTestItem()
            splash_item["href"] = a.xpath("./@href").extract_first()
            splash_item["text"] = a.xpath("./text()").extract_first()
            yield splash_item
