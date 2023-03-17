# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import pymongo
import scrapy
from scrapy.pipelines.images import ImagesPipeline

class CaipiaoPipeline:
    def open_spider(self, spider):
        self.f = open("./双色球.csv", mode="a", encoding='utf-8')

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        self.f.write(f"{item['qihao']}, {item['red_ball']}, {item['blue_ball']} \n")
        return item

class CaiPiaoMySQLPipeline:
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="数据库学习"
        )
    def close_spider(self, spider):
        if self.conn:
            self.conn.close()
    
    def process_item(self, item, spider):
        try:
            cursor = self.conn.cursor()
            sql = "insert into caipiao (qihao, 红色球, 蓝色球) values (%s, %s, %s)"

            cursor.execute(sql, (item["qihao"], item["red_ball"], item["blue_ball"]))
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            if cursor:
                cursor.close()
        return item

class CaiPiaoMongoDBPipeline:
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host="localhost", port=27017)
        db = self.client["python"]
        self.collection = db["caipiao"]
    
    def close_spider(self, spider):
        self.client.close()
    
    def process_item(self, item, spider):
        self.collection.insert_one({"qihao":item["qihao"], "红色球":item["red_ball"], "蓝色球":item["blue_ball"]})
        return item



