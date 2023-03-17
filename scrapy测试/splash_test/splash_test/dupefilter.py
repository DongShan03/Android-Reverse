from scrapy_redis.dupefilter import RFPDupeFilter as BaseRFPDupeFilter
from scrapy_splash.dupefilter import splash_request_fingerprint
from scrapy_redis_bloomfilter.dupefilter import RFPDupeFilter
from scrapy_redis_bloomfilter.defaults import BLOOMFILTER_HASH_NUMBER, BLOOMFILTER_BIT, DUPEFILTER_DEBUG
from scrapy_redis_bloomfilter import defaults
from scrapy_redis.connection import get_redis_from_settings
from scrapy_redis_bloomfilter.bloomfilter import BloomFilter
from scrapy_redis.dupefilter import RFPDupeFilter as BaseDupeFilter
import time

class MyDupefilter(BaseRFPDupeFilter):

    def __init__(self, server, key, debug, bit, hash_number):

        self.server = server
        self.key = key
        self.debug = debug
        self.bit = bit
        self.hash_number = hash_number
        self.logdupes = True
        self.bf = BloomFilter(server, self.key, bit, hash_number)
    
    @classmethod
    def from_settings(cls, settings):
        server = get_redis_from_settings(settings)

        # TODO: Use SCRAPY_JOB env as default and fallback to timestamp.
        key = defaults.DUPEFILTER_KEY % {'timestamp': int(time.time())}
        debug = settings.getbool('DUPEFILTER_DEBUG', DUPEFILTER_DEBUG)
        bit = settings.getint('BLOOMFILTER_BIT', BLOOMFILTER_BIT)
        hash_number = settings.getint('BLOOMFILTER_HASH_NUMBER', BLOOMFILTER_HASH_NUMBER)
        return cls(server, key=key, debug=debug, bit=bit, hash_number=hash_number)
    
    @classmethod
    def from_crawler(cls, crawler):
        instance = cls.from_settings(crawler.settings)
        return instance
    
    @classmethod
    def from_spider(cls, spider):
        settings = spider.settings
        server = get_redis_from_settings(settings)
        dupefilter_key = settings.get("SCHEDULER_DUPEFILTER_KEY", defaults.SCHEDULER_DUPEFILTER_KEY)
        key = dupefilter_key % {'spider': spider.name}
        debug = settings.getbool('DUPEFILTER_DEBUG', DUPEFILTER_DEBUG)
        bit = settings.getint('BLOOMFILTER_BIT', BLOOMFILTER_BIT)
        hash_number = settings.getint('BLOOMFILTER_HASH_NUMBER', BLOOMFILTER_HASH_NUMBER)
        print(key, bit, hash_number)
        instance = cls(server, key=key, debug=debug, bit=bit, hash_number=hash_number)
        return instance
    
    def request_fingerprint(self, request):
        return splash_request_fingerprint(request)

    def request_seen(self, request):
        fp = self.request_fingerprint(request)
        # This returns the number of values added, zero if already exists.
        if self.bf.exists(fp):
            return True
        self.bf.insert(fp)
        return False
    
    def log(self, request, spider):
        if self.debug:
            msg = "Filtered duplicate request: %(request)s"
            self.logger.debug(msg, {'request': request}, extra={'spider': spider})
        elif self.logdupes:
            msg = ("Filtered duplicate request %(request)s"
                   " - no more duplicates will be shown"
                   " (see DUPEFILTER_DEBUG to show all duplicates)")
            self.logger.debug(msg, {'request': request}, extra={'spider': spider})
            self.logdupes = False
        spider.crawler.stats.inc_value('bloomfilter/filtered', spider=spider)
