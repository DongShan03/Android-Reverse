from hashlib import sha256


input = "aid=728925286&auto_play=0&build=6240300&cid=786385874&did=LR0sHXxOeEBwQnFINEg0VjQFPVxvCjJXMQEwBWBXMQ&epid=&from_spmid=tm.recommend.0.0&ftime=1671724102&lv=0&mid=0&mobi_app=android&part=1&sid=0&spmid=main.ugc-video-detail.0.0&stime=1671770723&sub_type=0&type=3"

#2363ba787f31f74aef2c40a3c2ca924d33083f19338491c749dcede566b1e6a5
#2363ba787f31f74aef2c40a3c2ca924d33083f19338491c749dcede566b1e6a5
#KEY = fd6b639dbcff0c2a1b03b389ec763c4b
#IV = 77b07a672d57d64c


salt = "9cafa6466a028bfb"

obj = sha256()
obj.update(input.encode("utf-8"))
obj.update(salt.encode("utf-8"))

res = obj.hexdigest().lower()
print(res)

