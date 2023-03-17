from redis import Redis 

r = Redis(host="localhost", port=6379,
            db=3, decode_responses=True)


r.zadd("香烟", {"anme":10, "zhizhang":10})