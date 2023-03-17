from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

def aes_encrypt(data):
    key_str = "fd6b639dbcff0c2a1b03b389ec763c4b"

    iv_str = "77b07a672d57d64c"

    aes = AES.new(
        key=key_str.encode("utf-8"),
        mode=AES.MODE_CBC,
        iv=iv_str.encode("utf-8"),
    )
    raw = pad(data.encode("utf-8"), 16)
    aes_bytes = aes.encrypt(raw)
    return aes_bytes

input = "aid=728925286&auto_play=0&build=6240300&cid=786385874&did=LR0sHXxOeEBwQnFINEg0VjQFPVxvCjJXMQEwBWBXMQ&epid=&from_spmid=tm.recommend.0.0&ftime=1671724102&lv=0&mid=0&mobi_app=android&part=1&sid=0&spmid=main.ugc-video-detail.0.0&stime=1671771604&sub_type=0&type=3&sign=7415ab15027d372ab7af9eb92649d75a0b3c9af1587045ce22a470f48b8a8cf4"


result = aes_encrypt(input)
#[123,-116,112,105,-15,21,-57,-91,6,-76,20,79,-49
#[123, 140, 112, 105, 241, 21, 199, 165, 6, 180
bs = []
for item in result:
    if item > 127: 
        item -= 256
    bs.append(item)

print(bs)


"""
treeMap.put("did", com.bilibili.lib.biliid.utils.f.a.c(f2));

"""



