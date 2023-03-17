import scrapy


class A17kSpider(scrapy.Spider):
    name = '17k'
    allowed_domains = ['17k.com']
    start_urls = ['https://user.17k.com/www/bookshelf/']

    def start_requests(self):
        post_url = "https://passport.17k.com/ck/user/login" 
        username = "18979334079"
        pwd = "cheng521210"

        yield scrapy.FormRequest(
            url=post_url,
            formdata={
                "loginName": username,
                "password": pwd,
            },
            callback=self.parse
        )

    def parse(self, response):
        yield scrapy.Request(url=A17kSpider.start_urls[0], callback=self.parse_detail)
    
    def parse_detail(self, response):
        print(response.text)
