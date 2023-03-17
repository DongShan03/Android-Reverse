import hashlib 

data = "123456"
obj = hashlib.md5()
obj.update(data.encode("utf-8"))

res = obj.hexdigest()
print(res)

import random
import math
ele_list = []
for _ in range(10):
    ele = "%02x" % (math.floor(random.uniform(0, 16)))
    ele_list.append(ele)
data = "".join(ele_list)
print(data)
# ele_list = []
# for item in data:
# 		ele = hex(item)[2:].rjust(2, "0")
# 		ele_list.append(ele)
# res = "".join(ele_list)
# print(res)